# Lab record and navigation

The original brief contains no starter source files. `run_labs.py` reconstructs
the exercises, using the exact delivery and hospital tables in the brief. The
baseline is an explicitly synthetic deterministic regression dataset. Each lab
has its own `outputs/labs/lab_NN/terminal.txt`, plus its CSV/JSON artifacts.
Run a single exercise with `.venv\Scripts\python.exe run_labs.py --lab N`.
Run all with `.venv\Scripts\python.exe run_labs.py` after the mini-project.

|Lab|Code section in run_labs.py|Recorded evidence and observation|
|---|---|---|
|01 MLOps|number == 1|MAE and counts for 0.2/0.3/0.4, delivery table, observations CSV/XLSX. CSV cannot have sheets. execution/id/split preserve membership. One-row test R2 is undefined.|
|02 Introduction|number == 2|Actual file-store listing, baseline/delivery runs, params, metrics, artifacts. SQLite servers keep metadata in a DB rather than per-run files.|
|03 Tracking|number == 3|Runs connect to HTTP server. Experiment groups runs; a run is one execution; params are settings, metrics numeric measures, tags metadata, artifacts files, model a reloadable package.|
|04 Logging|number == 4|Exact 20 patients; train/test counts and actual/predicted/signed/absolute errors logged as tables and CSV. This is an educational regression, not a clinical predictor.|
|05 Multiple runs|number == 5|Nine seed/split comparisons; compare the three sizes at fixed seed. Training-size trends can be confounded by changing test membership.|
|06 Autologging|number == 6|Same data/configuration in one experiment. Automatic sklearn params/training metrics/model vs explicit test MAE/R2/model; comparison JSON records actual captured keys.|
|07 Server|number == 7 and two independent scripts|Same server and experiment; no separate server needed. Central tracking supports team provenance and comparison.|
|08 Models|number == 8|Logged model URI, reload through pyfunc, saved predictions on x=2,6,12.|
|09 Custom model|number == 9; hf_model.py; evaluate.py|Real custom Hugging Face model URI from mini-project; load and predict new short sentences through MLflow.|
|10 Evaluation|number == 10|Exact two experiment names; first logs MAE, second MAE/MSE/R2. MAE/MSE lower, R2 higher is better.|
|11 Registry|number == 11|With/without intercept candidates, lower-MAE champion alias, version printed on reload.|
|12 Projects|labs/lab_12/MLproject and train.py|Brief's second LAB 11 is treated as Lab12. Two actual mlflow run commands at 0.25/0.40, seed7, unchanged train.py.|
|13 Client|number == 13|Client searches Lab05, ascending MAE, max_results=3; shared server avoids copying databases.|
|14 CLI|number == 14|Actual version/help/experiment search output.|

Start tracking server from root:

```powershell
.\.venv\Scripts\python.exe -m mlflow server --host 127.0.0.1 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlartifacts
```

Lab07 scripts can be executed separately from root. Lab12 commands can be run
from its directory using the absolute project interpreter (activate the virtual
environment first so the MLproject `python` resolves correctly):

```powershell
.\.venv\Scripts\Activate.ps1
cd labs/lab_12
python -m mlflow run . --env-manager local -P test_size=0.25 -P random_state=7
python -m mlflow run . --env-manager local -P test_size=0.40 -P random_state=7
```

Interpretation: MAE is in target units; MSE squares those units; R2 compares to a
constant test-mean baseline and can be negative. Tiny delivery splits are unstable.
Saving exact row membership and seed is more useful than recording counts alone.
No quiz questions were included in the documents.
