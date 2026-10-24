param(
    [string]$CoconutPath = "",
    [string]$FloodPath = "",
    [string]$ScreeningPath = "",
    [string]$ReportDirectory = ""
)

$ErrorActionPreference = "Continue"
$SiteRoot = Split-Path -Parent $PSScriptRoot
$SiblingRoot = Split-Path -Parent $SiteRoot

if ([string]::IsNullOrWhiteSpace($CoconutPath)) { $CoconutPath = Join-Path $SiblingRoot "Coconut-Harvest-AI" }
if ([string]::IsNullOrWhiteSpace($FloodPath)) { $FloodPath = Join-Path $SiblingRoot "Flood-Rescue-AI" }
if ([string]::IsNullOrWhiteSpace($ScreeningPath)) { $ScreeningPath = Join-Path $SiblingRoot "Multimodal-Narcotics-Screening-AI" }
if ([string]::IsNullOrWhiteSpace($ReportDirectory)) { $ReportDirectory = Join-Path $SiteRoot "reports\local-checks" }

$projects = @(
    [pscustomobject]@{ Name = "Coconut Harvest AI"; Path = $CoconutPath },
    [pscustomobject]@{ Name = "Flood Rescue AI"; Path = $FloodPath },
    [pscustomobject]@{ Name = "Multimodal Narcotics Screening AI"; Path = $ScreeningPath }
)
$results = [System.Collections.Generic.List[object]]::new()
$runStarted = Get-Date

function Add-Result([string]$Project, [string]$Check, [string]$Status, [string]$Details) {
    $results.Add([pscustomobject]@{
        Timestamp = (Get-Date).ToString("o")
        Project = $Project
        Check = $Check
        Status = $Status
        Details = $Details
    })
    Write-Host ("[{0}] {1} - {2}: {3}" -f $Status, $Project, $Check, $Details)
}

function Invoke-LocalPython([string]$PythonExe, [string[]]$Arguments, [string]$WorkingDirectory) {
    Push-Location $WorkingDirectory
    try {
        & $PythonExe @Arguments
        return $LASTEXITCODE
    }
    finally {
        Pop-Location
    }
}

Write-Host "PUI89 shared local checks — no installs, downloads, network calls, or hosted runners."
Write-Host "Started: $($runStarted.ToString('yyyy-MM-dd HH:mm:ss'))"
Write-Host "Reports: $ReportDirectory"
Write-Host ""

foreach ($project in $projects) {
    $repo = $project.Path
    if (-not (Test-Path -LiteralPath $repo -PathType Container)) {
        Add-Result $project.Name "Repository path" "MISSING" "Not found: $repo. Pass the correct path with the matching parameter."
        continue
    }

    Add-Result $project.Name "Repository path" "OK" (Resolve-Path -LiteralPath $repo).Path

    if (-not (Test-Path -LiteralPath (Join-Path $repo "pyproject.toml") -PathType Leaf)) {
        Add-Result $project.Name "Project configuration" "WARN" "pyproject.toml not found; Python checks may be incomplete."
    }

    $pythonExe = Join-Path $repo ".venv\Scripts\python.exe"
    if (-not (Test-Path -LiteralPath $pythonExe -PathType Leaf)) {
        $pythonCommand = Get-Command "python" -ErrorAction SilentlyContinue
        if ($null -eq $pythonCommand) {
            Add-Result $project.Name "Python runtime" "SKIP" "Python not found. Install Python locally; this script will not install it."
            continue
        }
        $pythonExe = $pythonCommand.Source
    }
    Add-Result $project.Name "Python runtime" "OK" $pythonExe

    $compileTargets = @("src", "apps", "flood_robot", "tools", "scripts", "tests") |
        ForEach-Object { Join-Path $repo $_ } |
        Where-Object { Test-Path -LiteralPath $_ -PathType Container }

    if ($compileTargets.Count -gt 0) {
        $compileArgs = @("-m", "compileall", "-q") + $compileTargets
        $compileCode = Invoke-LocalPython $pythonExe $compileArgs $repo
        if ($compileCode -eq 0) {
            Add-Result $project.Name "Python syntax" "PASS" "compileall completed."
        } else {
            Add-Result $project.Name "Python syntax" "FAIL" "compileall exited with code $compileCode."
        }
    } else {
        Add-Result $project.Name "Python syntax" "SKIP" "No recognised Python source directories found."
    }

    $pytestCheck = Invoke-LocalPython $pythonExe @("-c", "import pytest") $repo 2>$null
    if ($pytestCheck -ne 0) {
        Add-Result $project.Name "Pytest suite" "SKIP" "pytest is not installed in this interpreter; no packages were installed."
        continue
    }

    if (-not (Test-Path -LiteralPath (Join-Path $repo "tests") -PathType Container)) {
        Add-Result $project.Name "Pytest suite" "SKIP" "No tests directory found."
        continue
    }

    $testCode = Invoke-LocalPython $pythonExe @("-m", "pytest", "-q") $repo
    if ($testCode -eq 0) {
        Add-Result $project.Name "Pytest suite" "PASS" "All discovered tests passed."
    } else {
        Add-Result $project.Name "Pytest suite" "FAIL" "pytest exited with code $testCode. Review the console output."
    }
}

# Check the static website's essential files without contacting any external service.
$siteFiles = @("index.html", "README.md")
foreach ($file in $siteFiles) {
    if (Test-Path -LiteralPath (Join-Path $SiteRoot $file) -PathType Leaf) {
        Add-Result "PUI89 Website" "Static file: $file" "PASS" "File exists."
    } else {
        Add-Result "PUI89 Website" "Static file: $file" "FAIL" "Required file missing."
    }
}

New-Item -ItemType Directory -Force -Path $ReportDirectory | Out-Null
$reportPath = Join-Path $ReportDirectory ("pui89-checks-{0}.csv" -f $runStarted.ToString("yyyyMMdd-HHmmss"))
$results | Export-Csv -LiteralPath $reportPath -NoTypeInformation -Encoding UTF8

$failed = @($results | Where-Object { $_.Status -eq "FAIL" }).Count
$missing = @($results | Where-Object { $_.Status -eq "MISSING" }).Count
$skipped = @($results | Where-Object { $_.Status -eq "SKIP" }).Count
Write-Host ""
Write-Host "Finished: $((Get-Date).ToString('yyyy-MM-dd HH:mm:ss'))"
Write-Host "Summary: $($results.Count) checks; $failed failed; $missing missing; $skipped skipped."
Write-Host "CSV report: $reportPath"
Write-Host "No model weights or datasets were downloaded. No robot hardware was controlled."
if ($failed -gt 0 -or $missing -gt 0) { exit 1 } else { exit 0 }
