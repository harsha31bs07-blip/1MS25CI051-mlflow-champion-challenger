# Final submission guide

Student: HARSHA BS | USN: 1MS25CI051 | Section: A
Prepared: 13 November 2026 | Re-verified from a fresh clone: 19 November 2026

## Files to use

| File | Purpose |
|---|---|
| Completed_Lab_Record.pdf | Visually reviewed 23-page record: project, 14 labs, quizzes and assessment table |
| Completed_Lab_Record.docx | Editable copy of the lab record |
| Completed_Quiz_Answers.pdf | Visually reviewed two-page quiz answer sheet |
| Completed_Quiz_Answers.docx | Editable quiz answer sheet |
| Submission.zip | Clean source, data, evidence, references, tests and documents |
| SUBMISSION_MANIFEST.json | SHA-256 and size of every packaged file except the manifest itself |
| Submission.sha256 | Checksum of the completed ZIP; kept alongside the ZIP |

Both quizzes are also included in the main lab record. Marks and instructor
signature/date are left for the instructor. The cover gives the course as
Skill Lab-II (CISL-2).

## Submission (21 November 2026)

1. Google Form "CISL-2 Skill Lab 2025 Batch": USN, name, section and the public
   repository link submitted; Google confirmed the response was recorded.
2. Lab book: Completed_Lab_Record.pdf and Completed_Quiz_Answers.pdf emailed to
   the instructor (deadline 23 November 2026).
3. For any regenerated copy, edit student.json, run build_documents.py,
   render_documents.py and make_submission.py, review the page images, then
   commit and push.

The repository is public and the final revision is pushed, so no separate
instructor access is needed. screenshots/prediction_terminal.png is a native
console capture of the Champion inference.

Repository: https://github.com/harsha31bs07-blip/1MS25CI051-mlflow-champion-challenger

## What was checked

On 13 November 2026 both original MLflow models reproduced all 60 saved
predictions, the Champion alias reproduced the eight new predictions and all 14
lab audits passed. An isolated fresh evaluation using the original exported local
model snapshots reproduced both prediction sequences and the Champion decision.

On 19 November 2026 the repository was cloned into an empty folder and README.md
was followed exactly: new virtual environment from the lock file, new tracking
store, evaluate.py, register_champion.py, predict_from_mlflow.py and run_labs.py.
All classification metrics (A macro-F1 0.966630, B 0.794286), both prediction
files, the disagreements table, the aliases (champion v1 = A, challenger v2 = B)
and the eight-row inference transcript matched the committed evidence exactly;
only latencies and run IDs differ. All 18 tests, verify_submission.py and all 14
lab audits passed. This run found and fixed a Lab 12 bug: when every lab runs in
one process, MLflow left MLFLOW_EXPERIMENT_ID set and the Project runs were
rejected; run_labs.py now clears it and a regression test covers it.

## Recreate on another computer

Extract the archive and follow README.md in order. The assignment excludes
tracking databases and model weights from submission, so a fresh machine must
install dependencies and execute evaluate.py, register_champion.py,
predict_from_mlflow.py and run_labs.py before live verification. Run run_labs.py
once per tracking store; a second run duplicates the lab runs. Existing run IDs
in saved evidence refer to the original local tracking store.

The ZIP excludes .venv, .idea, .git, caches, model weights, mlruns, mlartifacts,
databases and preview images. For a live demonstration in the viva, use a
tracking store produced by following README.md (under ten minutes on CPU once the
models are cached). The manifest lets the instructor verify the included files
without needing the local runtime.
