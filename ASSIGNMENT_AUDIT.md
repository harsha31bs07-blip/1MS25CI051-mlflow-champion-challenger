# Assignment audit

Audit date: 10 November 2026. Student: HARSHA BS, 1MS25CI051, Section A.

The implementation and saved evidence pass the checks below. The submission is
not yet fully ready for an instructor: course details, instructor access/LMS
submission, and a native terminal screenshot remain unresolved.

## Scope and sources

Reviewed both original assignment briefs, both subsequently supplied quiz/key
documents, source and helper scripts, tests, dependency files, datasets, recorded
CSV/JSON/text outputs, generated Word records, screenshots, Git tracking rules,
local history and the published repository revision. Local caches, installed
third-party packages and tracking-store internals are runtime dependencies rather
than student-authored submission source.

The independent checks are reproducible:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe verify_submission.py
.\.venv\Scripts\python.exe audit_labs.py
```

At this audit, pytest passes 15 tests. Verification reloads both actual MLflow
models and the Champion alias; it does not train replacement models, relog
artifacts, change aliases or rewrite the dependency snapshot. Its only output
mutation is the local verification report. The lab audit similarly writes only
its local report.

## Mini-project requirements

|Requirement|Evidence and result|
|---|---|
|Two models on identical saved inputs|Both prediction files preserve all 60 input texts and references in order; data hash matches the recorded evaluation.|
|Reproducibility|Seed, CPU device, batch size and maximum length recorded. Exact Hub revisions now pinned to the revisions used in the existing evaluation. Executed environment is retained in requirements-lock.txt.|
|Required three run names|Live tracking confirms both A/B sentiment runs and compare_sentiment, all FINISHED.|
|Parameters, metrics and tags|Required parameters and tags present. All four classification metrics independently recomputed; logged values and elapsed-time arithmetic checked. Student USN verified.|
|Rule declared before results|Initial Git commit preserves the 0.01 macro-F1 improvement margin and 5x latency guardrail. Those rule values are unchanged and agree with the saved manifest.|
|Correct decision|A retained: macro-F1 0.966630 versus B 0.794286. Winner and summary delta match the rule.|
|Registry aliases|Both aliases resolve to the exact evaluated run IDs, not merely matching A/B labels.|
|Logged artifacts|Prediction CSVs, references, metrics, README, requirements, confusion matrix and comparison chart verified in each candidate run.|
|Qualitative examples|12 disagreements saved; six specific comments in qualitative_analysis.csv, including a case where B is correct.|
|New-data inference|Eight disjoint inputs; saved text/IDs, model ID and version checked. Prediction replay through the Champion alias matches saved output. The script imports no Hugging Face pipeline.|
|Decision explanation|The saved explanation is within the required 150–250 words and discusses sample size and quality/speed trade-offs.|
|Repository structure and history|Required scripts/data/output folders present; at least three real commits precede this audit. No database, model weights or raw tracking-store paths are tracked in Git.|
|Screenshots|Comparison and registry images are genuine MLflow captures. The prediction image remains a labeled transcript rendering; a native terminal-window capture is still missing.|

## Labs and quizzes

All 14 lab branches have recorded execution evidence. `outputs/lab_audit.json`
records the checks for each lab. These include recomputation of the six Lab01
splits and nine Lab05 comparisons, exact hospital-table predictions, automatic
versus manual logging evidence, shared-server runs, sklearn model reload,
registry winner, both prescribed MLflow Project runs, top-three ranking and CLI
output. Lab01 CSV membership now includes an explicit dataset column alongside
execution, seed, test size, row ID and split; the workbook contains six sheets.

All 30 quiz responses match the supplied answer keys. Generated response sheets
contain the supplied student identity. These are completed response sheets, not
evidence of an instructor-awarded score.

The instructor's original starter scripts were not provided. The generic
regression baseline is a declared synthetic replacement, while the delivery and
hospital tables reproduce the brief. Quiz questions about particular teaching
scripts follow their supplied answer keys. Exact equivalence to those missing
scripts cannot be independently verified; provide them if exact matching is
required by the instructor.

## Fixes made during this audit

- Added a fresh-clone virtual-environment setup command and dependency constraints.
- Pinned both Hugging Face models to their already recorded source revisions.
- Reject missing columns, blank/non-string inputs, duplicate IDs/text and
  evaluation/new-data overlap after whitespace/case normalization.
- Strengthened checks for all metrics, artifacts, summary fields, exact registry
  run IDs and saved prediction versions; verification is now read-only on MLflow.
- Added direct quiz-key transcription tests and generated-document identity checks.
- Added explicit dataset membership to the Lab01 CSV/workbook and checked it.
- Added consistent Git line endings for data and source files.

No measured scores, decision rule, evaluation labels or historical commits were
altered. The AI-use declaration is retained. Ground rule 4 in the supplied brief
states: “If you use an AI assistant, say so in your README and be ready to explain
every line in a viva.” Removing that declaration would make this submission less
compliant with the assignment.

## Outstanding actions

1. Confirm course title and code; these remain explicitly pending.
2. Supply a native screenshot of the successfully executed PyCharm terminal.
   Desktop capture previously failed because its native helper was unavailable.
3. Give the instructor access to the private GitHub repository or choose public
   visibility; no instructor username has been supplied.
4. Submit the repository link at the correct LMS assignment. No LMS URL or
   submission receipt has been supplied.
5. Review the code and results for the viva. Supply missing teaching scripts if
   the instructor requires their exact implementation rather than equivalents.

The audit fixes are local. The GitHub repository's pre-audit published revision
was verified as d371ee925772680d12eaba7314164ae63fc84f67; this audit has not
published a new revision or submitted to the LMS.
