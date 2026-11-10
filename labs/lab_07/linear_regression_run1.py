"""Independent client one: same tracking server and experiment as client two."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import mlflow
from run_labs import track
mlflow.set_tracking_uri('http://127.0.0.1:5000')
track('Lab07-Shared-Server', 'intercept-True', intercept=True)
