# RELEASE RUSH
## Phase 2 — Build & Continuous Integration

**Total Marks: 25**

### INCIDENT: THE BROKEN BUILD PIPELINE

The development team has pushed a new version of the Inventory application.

The CI workflow starts successfully but fails during dependency installation.

The automated testing and build stages are never reached.

Your team has been assigned to investigate and restore the pipeline.

### OBJECTIVES

Investigate the failed build, identify the underlying configuration problem, restore dependency installation and demonstrate a successful CI pipeline.

### YOUR TASKS

1. Inspect the supplied build failure evidence.
2. Investigate the failed GitHub Actions workflow.
3. Examine the dependency configuration.
4. Investigate the dependency's Git history.
5. Identify and correct the build failure.
6. Install the required dependencies successfully.
7. Run the automated tests.
8. Generate the application build artifact.
9. Verify the complete CI pipeline succeeds.

---

### FILES PROVIDED

- `requirements.txt`
- `app.py`
- `tests/test_app.py`
- `build.py`
- `ci_check.py`
- `.github/workflows/ci.yml`
- `evidence/first-failed-run.log`

### PARTICIPANT SETUP

**Step 1 — Clone the official repository**

https://github.com/sammjoshuaa07-ui/ReleaseRush-Phase-2-Build-CI

```bash
git clone https://github.com/sammjoshuaa07-ui/ReleaseRush-Phase-2-Build-CI.git
cd ReleaseRush-Phase-2-Build-CI
```

**Step 2 — Create your team's repository**

The team leader must create a new, empty GitHub repository.

Suggested name:

`RR-TEAM-ID-Phase-2-Build-CI`

Do not add a README, Gitignore or license during creation.

**Step 3 — Configure your remotes**

```bash
git remote rename origin source
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Verify:

```bash
git remote -v
```

`origin` must point to your team's repository, and `source` must point to the official event repository.

**Step 4 — Push the starter repository**

```bash
git push -u origin main
```

Your team now has an independent copy with the original Git history.

The original failed workflow history is not copied to your repository. Use the supplied failure evidence to investigate the original incident. Your own workflow will run on your repository.

---

### CHALLENGE EXECUTION

**Step 5 — Investigate the failure**

Examine the supplied build failure log, dependency configuration, Git history and CI workflow.

Identify the stage at which the pipeline fails and establish the underlying reason.

**Step 6 — Repair the configuration**

Correct the dependency configuration without removing required dependencies or bypassing the installation stage.

Use the repository history and package information to support your decision.

**Step 7 — Validate locally**

Install the dependencies and run the supplied automated tests.

For example:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

**Step 8 — Generate the build artifact**

```bash
python build.py
```

Inspect the generated artifact and verify that the build completed successfully.

**Step 9 — Run the validation check**

```bash
python ci_check.py
```

Confirm that the application's build and validation checks succeed.

**Step 10 — Commit and push**

Commit the necessary corrections and push them to your team's repository:

```bash
git add .
git commit -m "fix: repair build pipeline"
git push origin main
```

**Step 11 — Verify GitHub Actions**

Open your team's GitHub repository and select the Actions tab.

Confirm that the latest workflow run completes successfully.

---

### SUBMISSION REQUIREMENTS

Submit:

1. Team ID and member names.
2. Your team's repository URL.
3. Failed pipeline stage.
4. Root cause of the failure.
5. Evidence supporting your diagnosis.
6. Description of the corrective action.
7. Successful dependency installation evidence.
8. Automated test output.
9. Build artifact verification.
10. Final commit hash.
11. Successful GitHub Actions run link.
12. Final release flag.

### RULES

- Teams of 2–3 members.
- Internet search is permitted.
- Work only within your own team.
- Do not remove required dependencies to bypass failures.
- Do not delete or weaken the supplied tests.
- Preserve the existing application functionality.
- Do not push to the official event repository or the `source` remote.
- All solutions must be committed and pushed to your own repository.

**Good luck!**
