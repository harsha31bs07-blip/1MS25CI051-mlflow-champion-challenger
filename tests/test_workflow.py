import ast
from pathlib import Path
import pandas as pd
import pytest
from evaluate import choose_winner, validate_data
from config import ROOT


def test_rule_boundaries():
    a = {'macro_f1': .8, 'avg_latency_ms': 10}
    assert choose_winner(a, {'macro_f1': .82, 'avg_latency_ms': 50}) == 'B'
    assert choose_winner(a, {'macro_f1': .82, 'avg_latency_ms': 51}) == 'A'
    assert choose_winner(a, {'macro_f1': .805, 'avg_latency_ms': 1}) == 'A'
    assert choose_winner(a, {'macro_f1': .8, 'avg_latency_ms': 1}) == 'A'
    assert choose_winner({'macro_f1': .81, 'avg_latency_ms': 10}, {'macro_f1': .82, 'avg_latency_ms': 10}) == 'B'


def test_dataset_contract():
    evaluation = pd.read_csv(ROOT / 'data/eval_inputs.csv')
    validate_data(evaluation, pd.read_csv(ROOT / 'data/new_data.csv'))
    assert evaluation.reference.value_counts().to_dict() == {'POSITIVE': 30, 'NEGATIVE': 30}


def test_prediction_script_uses_mlflow_only():
    tree = ast.parse((ROOT / 'predict_from_mlflow.py').read_text())
    imports = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    imports += [alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names]
    assert not any(m and ('transformers' in m or 'hf_model' in m) for m in imports)
    assert 'mlflow.pyfunc.load_model(uri)' in ast.unparse(tree)


@pytest.mark.parametrize('problem', ['missing_column', 'null_text', 'blank_text', 'duplicate_text', 'duplicate_id', 'overlap', 'too_few'])
def test_new_data_rejects_invalid_inputs(problem):
    evaluation = pd.read_csv(ROOT / 'data/eval_inputs.csv')
    new = pd.read_csv(ROOT / 'data/new_data.csv')
    if problem == 'missing_column':
        new = new.drop(columns='text')
    elif problem == 'null_text':
        new.loc[0, 'text'] = None
    elif problem == 'blank_text':
        new.loc[0, 'text'] = '   '
    elif problem == 'duplicate_text':
        new.loc[0, 'text'] = '  ' + new.loc[1, 'text'].upper() + ' '
    elif problem == 'duplicate_id':
        new.loc[0, 'id'] = new.loc[1, 'id']
    elif problem == 'overlap':
        new.loc[0, 'text'] = '  ' + evaluation.loc[0, 'text'].upper() + ' '
    else:
        new = new.head(4)
    with pytest.raises(ValueError):
        validate_data(evaluation, new)


def test_exact_assignment_tables_and_small_split():
    from run_labs import dataset, fit
    assert dataset('delivery').y.tolist() == [16, 19, 27, 29, 34]
    assert len(dataset('hospital')) == 20
    _, predictions, metrics, rows = fit('delivery', .2)
    assert len(predictions) == 1 and (rows.split == 'train').sum() == 4
    assert 'r2' not in metrics


def test_saved_lab_completion_and_ranking():
    assert all((ROOT / f'outputs/labs/lab_{n:02}/terminal.txt').exists() for n in range(1,15))
    top = pd.read_csv(ROOT / 'outputs/labs/lab_13/top_three.csv')
    assert len(top) == 3 and top.mae.is_monotonic_increasing
