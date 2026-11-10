# Genuine evidence to capture

Use http://127.0.0.1:5000 after execution. Screenshots must show actual runs.

1. `mlflow_compare.png`: open hf-sentiment-champion-challenger, select both A and B
   runs, Compare. Include names, macro_f1 and latency.
2. `registry_aliases.png`: Models > sentiment-model, show champion and challenger
   versions and their Hugging Face tags.
3. `prediction_terminal.png`: a clearly labeled browser rendering of the verbatim
   terminal transcript from predict_from_mlflow.py, including alias URI, model
   version/ID and all eight predictions. It is not a native console screenshot.
   If the instructor requires the console window itself, capture that window too.

The comparison and registry images capture the actual local MLflow UI. Text
evidence is also saved in outputs/prediction_terminal.txt, metrics_summary.json
and registry.json. Regenerate with capture_evidence.py (optional evidence dependencies).

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-evidence.txt
.\.venv\Scripts\python.exe capture_evidence.py
```

The screenshot script launches installed Microsoft Edge with an isolated headless
profile, opens only the local MLflow server, and renders the saved transcript.
