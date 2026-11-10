"""Assignment entry point for Lab 2; implementation is shared in run_labs.py."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import mlflow
from config import TRACKING_URI
from run_labs import run_lab

if __name__ == '__main__':
    mlflow.set_tracking_uri(TRACKING_URI)
    run_lab(2)

