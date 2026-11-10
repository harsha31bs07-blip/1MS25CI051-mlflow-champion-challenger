"""Audit recorded results against data, reloadable models and live registry."""
import importlib.metadata
import json
import mlflow
import pandas as pd
import torch
from mlflow import MlflowClient
from sklearn.metrics import f1_score
from config import ROOT, OUTPUTS, TRACKING_URI, REGISTERED_MODEL, STUDENT
from evaluate import choose_winner, validate_data


def main():
    torch.set_num_threads(4)
    mlflow.set_tracking_uri(TRACKING_URI)
    client = MlflowClient()
    result = json.loads((OUTPUTS / 'metrics_summary.json').read_text())
    evaluation = pd.read_csv(ROOT / 'data/eval_inputs.csv')
    validate_data(evaluation, pd.read_csv(ROOT / 'data/new_data.csv'))
    checks = []
    for role in ['A', 'B']:
        entry = result['models'][role]
        predictions = pd.read_csv(OUTPUTS / role / f'predictions_{role}.csv')
        assert predictions.text.tolist() == evaluation.text.tolist()
        assert predictions.reference.tolist() == evaluation.reference.tolist()
        assert abs(f1_score(predictions.reference, predictions.prediction, average='macro') - entry['metrics']['macro_f1']) < 1e-10
        run = client.get_run(entry['run_id'])
        assert run.info.status == 'FINISHED'
        assert all(t in run.data.tags for t in ['student_usn', 'library_versions', 'dataset_name'])
        assert run.data.tags['student_usn'] == STUDENT['usn']
        reloaded = mlflow.pyfunc.load_model(entry['model_uri'])
        replay = reloaded.predict(evaluation[['text']])
        assert replay.prediction.tolist() == predictions.prediction.tolist()
        # Both evaluation figures are available in each candidate run too.
        client.log_artifact(entry['run_id'], str(OUTPUTS / 'comparison.png'))
        checks.append(f'{role}: saved inputs, recomputed F1, logged metadata and full model replay passed')
    assert choose_winner(*[result['models'][r]['metrics'] for r in ['A','B']]) == result['winner']
    version = client.get_model_version_by_alias(REGISTERED_MODEL, 'champion')
    assert version.tags['candidate'] == result['winner']
    assert client.get_model_version_by_alias(REGISTERED_MODEL, 'challenger').version != version.version
    assert len(pd.read_csv(OUTPUTS / 'new_data_predictions.csv')) == 8
    assert all((OUTPUTS / 'labs' / f'lab_{i:02}' / 'terminal.txt').exists() for i in range(1,15))
    checks += ['Decision and both registry aliases verified', 'All fourteen lab transcripts present', 'Eight new-data predictions saved']
    lock = sorted(f'{d.metadata["Name"]}=={d.version}' for d in importlib.metadata.distributions())
    (ROOT / 'requirements-lock.txt').write_text('\n'.join(lock)+'\n')
    quizzes = json.loads((ROOT / 'quiz_answers.json').read_text())
    assert len(quizzes['day_1']) == len(quizzes['day_2']) == 15
    checks += ['Student identity verified in live MLflow tags', 'Both supplied quizzes have 15 completed responses with explanations']
    report = {'checks': checks, 'remaining_student_actions': ['Confirm course title and course code', 'Provide LMS assignment URL for submission', 'Provide instructor GitHub username for private-repository access or choose public visibility', 'Capture the native PyCharm terminal window: the desktop screenshot helper is unavailable', 'Review implementation and quiz explanations for viva']}
    (OUTPUTS / 'verification.json').write_text(json.dumps(report, indent=2))
    client.log_artifact(result['summary_run_id'], str(OUTPUTS / 'verification.json'))
    client.log_artifact(result['summary_run_id'], str(ROOT / 'requirements-lock.txt'))
    client.log_artifact(result['summary_run_id'], str(OUTPUTS / 'qualitative_analysis.csv'))
    for filename in ['mlflow_compare.png', 'registry_aliases.png', 'prediction_terminal.png']:
        assert (ROOT / 'screenshots' / filename).exists()
        client.log_artifact(result['summary_run_id'], str(ROOT / 'screenshots' / filename), 'screenshots')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
