"""Resolve a registry alias; no fixed version is needed."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import mlflow
import pandas as pd
from mlflow import MlflowClient
from config import TRACKING_URI

if __name__ == '__main__':
    mlflow.set_tracking_uri(TRACKING_URI)
    uri = 'models:/lab-regression@champion'
    version = MlflowClient().get_model_version_by_alias('lab-regression', 'champion')
    print('Loaded', uri, 'version', version.version)
    print(mlflow.pyfunc.load_model(uri).predict(pd.DataFrame({'x': [3., 7.]})))
