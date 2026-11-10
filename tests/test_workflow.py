import ast
from pathlib import Path
import pandas as pd
from evaluate import choose_winner, validate_data
from config import ROOT


def test_rule_boundaries():
    a = {'macro_f1': .8, 'avg_latency_ms': 10}
    assert choose_winner(a, {'macro_f1': .82, 'avg_latency_ms': 50}) == 'B'
    assert choose_winner(a, {'macro_f1': .82, 'avg_latency_ms': 51}) == 'A'
    assert choose_winner(a, {'macro_f1': .805, 'avg_latency_ms': 1}) == 'A'
    assert choose_winner(a, {'macro_f1': .8, 'avg_latency_ms': 1}) == 'A'


def test_dataset_contract():
    evaluation = pd.read_csv(ROOT / 'data/eval_inputs.csv')
    validate_data(evaluation, pd.read_csv(ROOT / 'data/new_data.csv'))
    assert evaluation.reference.value_counts().to_dict() == {'POSITIVE': 30, 'NEGATIVE': 30}


def test_prediction_script_uses_mlflow_only():
    tree = ast.parse((ROOT / 'predict_from_mlflow.py').read_text())
    imports = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    assert not any(m and ('transformers' in m or 'hf_model' in m) for m in imports)
    assert 'mlflow.pyfunc.load_model(uri)' in ast.unparse(tree)
