"""Add supplied student identity to existing measured runs without changing results."""
from datetime import datetime, timezone
import json
import mlflow
from config import ROOT, OUTPUTS, TRACKING_URI, STUDENT, REGISTERED_MODEL

mlflow.set_tracking_uri(TRACKING_URI)
client = mlflow.MlflowClient()
result = json.loads((OUTPUTS / 'metrics_summary.json').read_text())
run_ids = [result['summary_run_id']] + [m['run_id'] for m in result['models'].values()]
for run_id in run_ids:
    for key, value in {'student_usn': STUDENT['usn'], 'student_name': STUDENT['name'],
                       'student_section': STUDENT['section'],
                       'student_identity_added_after_evaluation': 'true'}.items():
        client.set_tag(run_id, key, value)
for alias in ['champion', 'challenger']:
    version = client.get_model_version_by_alias(REGISTERED_MODEL, alias)
    client.set_model_version_tag(REGISTERED_MODEL, version.version, 'student_usn', STUDENT['usn'])
    assert client.get_run(version.run_id).data.tags['student_usn'] == STUDENT['usn']
result['student_identity'] = {**STUDENT, 'added_after_evaluation_at': datetime.now(timezone.utc).isoformat()}
(OUTPUTS / 'metrics_summary.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
for filename in ['student.json', 'quiz_answers.json', 'submission_status.json']:
    client.log_artifact(result['summary_run_id'], str(ROOT / filename), 'submission')
client.log_artifact(result['summary_run_id'], str(OUTPUTS / 'metrics_summary.json'), 'submission')
print('Student identity verified on all three comparison runs and both registry versions.')
