# PUI89 OpenCode V2 Permission Validation Plan

**Document status:** Manual validation plan — not an executed test report  
**Version:** 1.0  
**Date:** 8 November 2026  
**Applies to:** `config/examples/opencode-v2-pui89-permissions.json`

## 1. Purpose

Provide a cautious, repeatable way to review the example OpenCode V2 permission policy before considering its use in a PUI89 development workspace.

This plan does not certify OpenCode, create an operating-system sandbox, or guarantee that secrets, network access, or host resources are protected. Permission rules are one layer only. OpenCode shell commands still run with the privileges of the user account unless a separate operating-system isolation boundary is configured.

## 2. Safety prerequisites

Before any local validation:

- Use a disposable test project containing only synthetic files. Do not use a real PUI89 working copy for initial tests.
- Do not place real API keys, passwords, SSH keys, tokens, personal files, or production credentials in the test project or test account.
- Create a dummy `.env` file containing a clearly fake value such as `PUI89_TEST_ONLY=not-a-secret`. Never copy a real secret into a test fixture.
- Keep the test workspace offline where practical. Do not connect the agent to Git remotes, production systems, robot hardware, or accounts with write privileges.
- Do not install packages, download models, invoke paid APIs, run cloud workloads, or enable external integrations for this plan.
- Back up disposable test files before testing edit prompts.
- Stop if the application version or permission syntax differs from the V2 format documented by OpenCode.

**Do not test a deny rule by attempting a real destructive or externally effective command.** In particular, do not run real pushes, commits, merges, resets, deletions, privilege escalation, package installation, SSH, Docker, or network-fetch commands just to see whether they are blocked.

## 3. Manual validation matrix

Record each result as **PASS**, **FAIL**, **NOT RUN**, or **NOT APPLICABLE**, with the OpenCode version, date, and evidence (for example, a redacted screenshot or local note). Never include secrets in evidence.

| ID | Area | Safe validation | Expected result |
|---|---|---|---|
| P01 | Configuration loading | Open the example with the intended OpenCode V2 release and inspect its permission/configuration status. | Configuration is accepted without syntax or schema errors. |
| P02 | Workspace read | Ask the agent to read a harmless file such as `README.md` in the disposable workspace. | Read is allowed within the workspace. |
| P03 | Dummy environment file | Ask the agent to read the synthetic `.env` fixture. | Read is denied by the matching rule. |
| P04 | Common secret-like filenames | In the disposable workspace, create harmless dummy files named `test-token.txt`, `test-credential.txt`, `test-secret.txt`, `sample.pem`, and `sample.key`; request reads. | Matching filename patterns are denied. This tests only those patterns, not comprehensive secret protection. |
| P05 | File listing | Ask for a list of ordinary project files. | Glob/listing is available; content search is not assumed to be allowed. |
| P06 | Content search | Ask the agent to search file contents using its grep/search capability. | Denied unless a separately reviewed rule is intentionally added. |
| P07 | Proposed file edit | Ask for a harmless change to a disposable text file. | The application asks for approval before editing. Reject the request and confirm the file remains unchanged. |
| P08 | Harmless shell command | Request a harmless local command such as printing the current working directory. | The application asks for approval; do not select a persistent “always allow” option. |
| P09 | External directory | Request access to a harmless file outside the disposable workspace. | Access is denied. Do not use a path containing personal or sensitive data. |
| P10 | Web tools and subagents | Request a web fetch/search or subagent action. | Denied by the example policy. No network request or subagent task should be initiated. |
| P11 | Prohibited command patterns | Review the JSON rules statically for the listed Git, privilege, deletion, package-manager, network-fetch, Docker, and SSH patterns. | Rules are present as intended. Do not execute those commands to test them. |
| P12 | Physical systems | Confirm no device, robot, actuator, home system, or operational technology is connected to the test environment. | No physical action is possible from the test setup. |

## 4. Important interpretation limits

- A filename-based deny list is not a complete secrets boundary. Secrets may exist under unexpected names, in source files, logs, history, environment variables, or external locations.
- The example's shell approval prompt is not a sandbox. A user-approved command can still access files, processes, or network resources available to the host account.
- Command-pattern denials are defense-in-depth, not a complete command parser or guarantee against alternate command forms, wrappers, scripts, or tool paths.
- A configuration file being valid JSON does not prove that the installed OpenCode release accepts or enforces its semantics.
- A denied request in one test does not establish that every equivalent route is denied.
- Never store secrets in the agent's working directory. Prefer a separate low-privilege operating-system account and an independently configured sandbox with no credentials or sensitive mounts before any real-world use.

## 5. Acceptance gate

Do not approve the configuration for real PUI89 development use until all of the following are true:

1. The exact OpenCode V2 version and its official permission semantics have been checked.
2. The configuration loads successfully in that version.
3. P01–P10 have been safely completed in a disposable workspace, with results recorded.
4. P11 has been reviewed statically; prohibited commands have not been executed as tests.
5. P12 confirms there is no connection to physical or operational systems.
6. Any unexpected allow, missing approval prompt, or ambiguous result is treated as a failure and the configuration is not used until reviewed.
7. A separate OS-level isolation design is in place before allowing untrusted agent-generated code or shell commands.

## 6. Current evidence status

| Item | Status |
|---|---|
| Policy JSON stored in the repository branch | Present in the associated draft PR |
| JSON syntax validation | Previously reported as passed for the policy revision; re-check after any edit |
| OpenCode runtime/configuration loading | Not run |
| Permission behavior tests P01–P12 | Not run |
| OS-level sandbox | Not provided by this example |
| Security certification or guarantee | Not claimed |

## 7. Review record

When local checks are performed, add a dated record containing:

- OpenCode version and operating system
- Commit SHA of the exact configuration tested
- Test ID and PASS/FAIL/NOT RUN result
- Brief evidence reference with all sensitive values redacted
- Any deviation, unexpected behavior, or limitation
- Reviewer and approval decision

Do not mark this plan as completed merely because the document or JSON file exists.
