# One-command automation for all PUI89 projects

This is a **local-first coordinator** for the three independent project repositories. It runs the checks together on the user's Windows computer, records a CSV report, and does not install dependencies or download data/models.

## What it checks

- Coconut Harvest AI: Python syntax and the existing pytest suite, if pytest is already installed in the selected interpreter.
- Flood Rescue AI: Python syntax and the existing pytest suite, if pytest is already installed.
- Multimodal Narcotics Screening AI: Python syntax and the existing pytest suite, if pytest is already installed.
- PUI89 website: required static files exist.
- A CSV status report records PASS, FAIL, SKIP, MISSING and WARN results.

The script uses each repository's local `.venv\Scripts\python.exe` when present, otherwise the Python executable on PATH. Missing dependencies are reported rather than installed automatically.

## Run on Windows

Save/clone all four repositories under one parent folder, for example:

```text
C:\PUI89\
  Pui89.github.io\
  Coconut-Harvest-AI\
  Flood-Rescue-AI\
  Multimodal-Narcotics-Screening-AI\
```

Open PowerShell in the website repository and run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\tools\run-all-project-checks.ps1
```

If your folders are elsewhere, pass their exact paths:

```powershell
.\tools\run-all-project-checks.ps1 `
  -CoconutPath "C:\path\to\Coconut-Harvest-AI" `
  -FloodPath "C:\path\to\Flood-Rescue-AI" `
  -ScreeningPath "C:\path\to\Multimodal-Narcotics-Screening-AI"
```

Reports are written to `reports\local-checks\` and are intentionally local output; they are not automatically committed or uploaded.

## Free-first and safety boundaries

- No GitHub Actions runner is launched by this script.
- No pip install, model download, dataset download, cloud API, subscription, or paid service is invoked.
- Tests can fail if a repository's dependencies are missing or incompatible. The script reports this rather than concealing it.
- Passing software tests does not prove model accuracy, field rescue performance, chemical identification, harvest safety, or physical robot capability.
- This script does not actuate or connect to robot hardware.
- Each project remains separate; this script coordinates checks, not model weights or data labels.

## What is not automated yet

Training is deliberately not triggered automatically: each project first needs a verified, properly licensed dataset and a documented baseline. Large downloads and GPU-heavy runs remain explicit, manual steps to avoid surprise storage, compute, or billing costs.
