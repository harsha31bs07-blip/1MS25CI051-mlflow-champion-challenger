"""Run all Lab 01 splits and persist metrics, observations and workbook sheets."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from run_labs import run_lab

if __name__ == '__main__':
    run_lab(1)

