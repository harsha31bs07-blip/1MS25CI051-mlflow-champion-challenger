# MLflow Skill Lab: all 14 labs and Champion–Challenger project

Student name: TO BE FILLED BY STUDENT  
USN: set the STUDENT_USN environment variable before your submission run.  
Course/section: TO BE FILLED BY STUDENT.

## Task and models

Binary English sentiment classification on 60 fixed, balanced, original labeled
sentences. A (current Champion): `distilbert/distilbert-base-uncased-finetuned-sst-2-english`.
B (Challenger): `M-FAC/bert-tiny-finetuned-sst2`. Both are pretrained Hugging Face
sentiment models. The brief permits substitute models for the same task; the tiny
Challenger explores quality versus CPU efficiency. Data provenance: `data/README.md`.

## Champion rule — declared before execution

Primary metric: macro-F1, higher is better. Promote B only if B minus A macro-F1
is at least **0.01** AND B's warm mean per-example latency is at most **5 times** A's.
Otherwise retain A, including exact ties and differences below the margin.
The one percentage-point margin avoids replacing a model for a negligible score
change; it is an operational threshold, not a statistical significance test. The
latency limit prevents an excessive runtime regression. Accuracy, macro precision,
macro recall and F1 are higher-is-better; latency and model size are lower-is-better.
This text and `config.RULE` are fixed before the final run. A SHA-256 copy of this
README and the input data is logged with every comparison.

## How to run (PowerShell, from repository root)

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:STUDENT_USN = 'YOUR_USN'
.\.venv\Scripts\python.exe -m mlflow server --host 127.0.0.1 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlartifacts
```

Keep that terminal running. In a second terminal:

```powershell
$env:MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
.\.venv\Scripts\python.exe evaluate.py
.\.venv\Scripts\python.exe register_champion.py
.\.venv\Scripts\python.exe predict_from_mlflow.py
.\.venv\Scripts\python.exe run_labs.py
.\.venv\Scripts\python.exe -m pytest -q
```

First downloads need Internet; saved MLflow models bundle tokenizer and weights
for offline reload. CPU, seed 42, batch size 8 and maximum 128 tokens are fixed.
Model download/load and one warm-up call are excluded from timing; elapsed time
is measured around evaluation inference only. Full environment is saved to
`requirements-lock.txt`. See `labs/README.md` for each exercise and commands.

## Results table and decision

Written from measured outputs by `evaluate.py` into `outputs/results.md`, and
included below after execution. The decision follows the rule above unchanged.

<!-- RESULTS_START -->
Execution pending.
<!-- RESULTS_END -->

## Limitations and declaration

This convenience sample is small, balanced and not randomly drawn from a target
population. Scores may reflect dataset construction and pretrained training overlap
cannot be ruled out. CPU timing varies with machine load and batching; it is not a
production benchmark. Confidence scores are not calibrated probabilities. Both
models may miss sarcasm, context or domain-specific language. No test data is used
for training or threshold selection. AI assistance (OpenAI Codex) was used to read
requirements, author data, implement code, debug and write explanations. The student
must review and understand every line, supply identity, and explain the choices in
the viva. Quiz questions were not supplied; no answers or marks are invented.

## Submission

Use repository name `<USN>-mlflow-champion-challenger`. Commit source/data/outputs
but exclude `.venv`, model weights, tracking databases, `mlruns` and `mlartifacts`.
Capture the three genuine screenshots described in `screenshots/README.md`.
GitHub publication and LMS submission require the student's account and identity.

References: [MLflow PythonModel](https://mlflow.org/docs/latest/ml/model/python_model/),
[MLflow registry](https://mlflow.org/docs/latest/ml/model-registry/), and each
candidate's Hugging Face model card. The missing metrics table in the brief is
handled with standard binary classification metrics, averaged over both labels.
