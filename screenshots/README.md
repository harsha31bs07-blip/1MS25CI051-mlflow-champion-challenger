# Genuine evidence to capture

Use http://127.0.0.1:5000 after execution. Screenshots must show actual runs.

1. `mlflow_compare.png`: open hf-sentiment-champion-challenger, select both A and B
   runs, Compare. Include names, macro_f1 and latency.
2. `registry_aliases.png`: Models > sentiment-model, show champion and challenger
   versions and their Hugging Face tags.
3. `prediction_terminal.png`: terminal running predict_from_mlflow.py, including
   alias URI, version/model ID and predictions.

Text evidence is also saved in outputs/prediction_terminal.txt, metrics_summary.json
and registry.json. It does not replace the required UI screenshots.
