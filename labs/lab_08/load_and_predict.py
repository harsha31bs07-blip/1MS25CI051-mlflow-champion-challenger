"""Reload the recorded Lab08 model without training."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import mlflow
import pandas as pd
from config import ROOT, TRACKING_URI

if __name__ == '__main__':
    mlflow.set_tracking_uri(TRACKING_URI)
    uri = (ROOT / 'outputs/labs/lab_08/model_uri.txt').read_text()
    model = mlflow.pyfunc.load_model(uri)
    data = pd.DataFrame({'x': [2., 6., 12.]})
    data['prediction'] = model.predict(data)
    print('Loaded', uri)
    print(data.to_string(index=False))
