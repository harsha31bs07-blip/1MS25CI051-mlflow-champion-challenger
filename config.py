"""Shared configuration. Set STUDENT_USN and MLFLOW_TRACKING_URI as needed."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / 'outputs'
TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI', 'http://127.0.0.1:5000')
EXPERIMENT = 'hf-sentiment-champion-challenger'
REGISTERED_MODEL = 'sentiment-model'
SEED = 42
MODEL_A = 'distilbert/distilbert-base-uncased-finetuned-sst-2-english'
MODEL_B = 'M-FAC/bert-tiny-finetuned-sst2'
RULE = {'primary_metric': 'macro_f1', 'margin': 0.01, 'max_latency_ratio': 5.0}
