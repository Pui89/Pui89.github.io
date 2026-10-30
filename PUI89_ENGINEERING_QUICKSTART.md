# PUI89 Engineering Quickstart

A local-first workflow for the three PUI89 AI application and robotics-concept repositories.

## 1. Folder layout

Place the four repositories side by side:

```text
PUI89-workspace/
├── PUI89.github.io/
├── Coconut-Harvest-AI/
├── Extreme-Flood-Rescue-AI/
└── Multimodal-Narcotics-Screening-AI/
```

The runner is in the website repository at `tools/pui89_dev.py`.

## 2. Run all project checks with one command

From the workspace folder:

```powershell
python .\PUI89.github.io\tools\pui89_dev.py --projects-root .
```

It runs each project's existing pytest suite and runs Ruff only if Ruff is already installed in that Python environment. It does not install packages, download models, call external APIs, or use cloud GPUs.

Reports are written to `pui89-reports/pui89-report.json` and `pui89-reports/pui89-report.csv`.

To check repository discovery without running tests:

```powershell
python .\PUI89.github.io\tools\pui89_dev.py --projects-root . --skip-tests
```

If your folders are named differently, rename the folders to the names above or adjust the `PROJECTS` mapping in the script. Use a Python environment with each project's test dependencies installed; this runner deliberately does not alter environments.

## 3. Optional local quality tools

Install only when wanted, in a project development environment:

```powershell
python -m pip install ruff pre-commit
pre-commit install
pre-commit run --all-files
```

The repositories already contain pre-commit configuration. Hooks may fetch their pinned open-source packages on first use. Review package versions and licences before installing.

## 4. Suggested daily cycle

1. Pull the latest changes.
2. Make one small change on a feature branch.
3. Run the affected project's tests.
4. Run the cross-project runner before opening a pull request.
5. Inspect the JSON/CSV reports; fix failures rather than hiding or relabelling them.
6. Open a pull request and wait for the repository's existing CI checks.
7. Merge only after reviewing the diff and successful checks.

## 5. Report interpretation and limits

- `PASS` means the command exited successfully; it does not prove real-world performance.
- `FAIL`, `ERROR`, and `TIMEOUT` require investigation.
- `SKIPPED` means a check did not run (for example, Ruff is not installed).
- `MISSING` means a repository folder was not found.
- A missing or skipped check must never be reported as a pass.
- This runner does not evaluate detector accuracy, robot hardware, sensor calibration, safety certification, or physical mission capability.

## 6. Resource and cost policy

Keep routine development local and lightweight. Do not add paid APIs, cloud GPU jobs, automatic model downloads, or large model dependencies to this workflow. GitHub-hosted CI may consume plan usage; check account limits and repository settings before enabling additional workflows.
