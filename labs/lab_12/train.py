"""Lab 12 project entry point; keep unchanged between the two prescribed runs."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from run_labs import track
from config import TRACKING_URI
import mlflow

parser = argparse.ArgumentParser()
parser.add_argument('--test-size', type=float, default=.25)
parser.add_argument('--random-state', type=int, default=7)
args = parser.parse_args()
mlflow.set_tracking_uri(TRACKING_URI)
track('Lab12-Projects', f'test-{args.test_size}', test_size=args.test_size, seed=args.random_state)
