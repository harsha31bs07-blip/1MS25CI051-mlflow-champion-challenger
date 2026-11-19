# Genuine evidence to capture

Use http://127.0.0.1:5000 after execution. Screenshots must show actual runs.

1. `mlflow_compare.png`: open hf-sentiment-champion-challenger, select both A and B
   runs, Compare. Include names, macro_f1 and latency.
2. `registry_aliases.png`: Models > sentiment-model, show champion and challenger
   versions and their Hugging Face tags.
3. `prediction_terminal.png`: a native Windows console capture of
   predict_from_mlflow.py loading `models:/sentiment-model@champion` and printing
   version 1, the Hugging Face model ID and all eight predictions. It was taken on
   19 November 2026 during a fresh-clone re-execution of the README steps; the
   printed table is identical to outputs/prediction_terminal.txt. MLflow's
   informational hint and type-hint warning appear above it, as they did in the run.

The comparison and registry images capture the actual local MLflow UI. Text
evidence is also saved in outputs/prediction_terminal.txt, metrics_summary.json
and registry.json. Regenerate the two UI images with capture_evidence.py (optional
evidence dependencies); it writes a transcript rendering to the git-ignored
prediction_transcript.png and leaves the console capture unchanged.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-evidence.txt
.\.venv\Scripts\python.exe capture_evidence.py
```

The screenshot script launches installed Microsoft Edge with an isolated headless
profile, opens only the local MLflow server, and renders the saved transcript.
