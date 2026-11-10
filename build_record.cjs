// Build a readable Word lab record from measured evidence and supplied identity.
const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, PageBreak, ImageRun,
        Footer, PageNumber, AlignmentType } = require('./.artifact-tools/node_modules/docx');
const root = __dirname;
const student = JSON.parse(fs.readFileSync(path.join(root, 'student.json'), 'utf8'));
const quizzes = JSON.parse(fs.readFileSync(path.join(root, 'quiz_answers.json'), 'utf8'));
const text = p => fs.readFileSync(path.join(root,p), 'utf8').replace(/\r\n/g,'\n');
const children = [];
function para(value, options={}) { children.push(new Paragraph({children:[new TextRun(value)], spacing:{after:120}, ...options})); }
function heading(value) { para(value,{heading:HeadingLevel.HEADING_1}); }
function code(value) { for(const line of value.split(/\r?\n/)) para(line,{spacing:{after:30}, children:[new TextRun({text:line,font:'Consolas',size:17})]}); }
function page() { children.push(new Paragraph({children:[new PageBreak()]})); }
para('MLflow Skill Lab Completed Record',{heading:HeadingLevel.TITLE});
para('Labs 01 through 14 and Champion Challenger Mini Project',{heading:HeadingLevel.SUBTITLE});
para('Prepared from actual local executions on 10 November 2026');
para(`Student name: ${student.name}    USN: ${student.usn}`);
para(`Section: ${student.section}    Course: ${student.course_title}    Code: ${student.course_code}`);
para('Repository: https://github.com/harsha31bs07-blip/1MS25CI051-mlflow-champion-challenger');
para('This record accompanies executable source, labeled data, tracked models and saved outputs. DistilBERT remains the Champion on the fixed sixty sentence evaluation set. All fourteen labs have separate terminal transcripts and the project reloads its Champion by registry alias.');
para('The original documents supplied no starter scripts. Equivalent solutions were implemented with the exact delivery and hospital datasets from the brief; the general baseline uses a declared synthetic dataset. The duplicated Projects heading is treated as Lab 12. The two subsequently supplied quizzes are answered with explanations in this record and in a separate response sheet.');
para('AI declaration: OpenAI Codex assisted with requirements, data authoring, implementation, execution and explanations. The student must review the code and be able to explain it in the viva. Instructor marks and signatures are intentionally unfilled.');
heading('Navigation');
para('Project: README.md, evaluate.py, hf_model.py, register_champion.py and predict_from_mlflow.py. Labs: run_labs.py and labs/README.md. Complete outputs: outputs/ and outputs/labs/lab_NN/.');
page(); heading('Mini Project Method and Decision');
const readme = text('README.md');
const rule = readme.split('## Champion rule')[1].split('## How to run')[0];
for(const line of rule.split('\n').filter(Boolean)) para(line.replace(/\*\*/g,''));
const result = JSON.parse(text('outputs/metrics_summary.json'));
for(const role of ['A','B']) {
 para(`${role} — ${result.models[role].hf_model_id}`,{heading:HeadingLevel.HEADING_2});
 for(const [key,value] of Object.entries(result.models[role].metrics)) para(`${key}: ${Number(value).toFixed(6)}`);
}
para(text('outputs/results.md').split('\n\n').slice(1).join('\n\n'));
page(); heading('Mini Project Visual Evidence');
for(const file of ['outputs/comparison.png']) {
 para(file);
 children.push(new Paragraph({children:[new ImageRun({type:'png',data:fs.readFileSync(path.join(root,file)),transformation:{width:590,height:file.includes('comparison')?275:400}})]}));
}
para('Confusion matrices A left and B right');
children.push(new Paragraph({children:['A','B'].map(r=>new ImageRun({type:'png',data:fs.readFileSync(path.join(root,`outputs/${r}/confusion_matrix.png`)),transformation:{width:290,height:218}}))}));
const topics = ['Introduction to MLOps','Introduction to MLflow','Tracking','Logging Functions','Multiple Experiments and Runs','Autologging','Tracking Server','Models','Custom Models','Model Evaluation','Model Registry','Projects','MLflow Client','MLflow CLI'];
const observations = [
'Six baseline/delivery splits are recorded. The five supplied delivery rows give four training rows and one test row at test_size 0.2; R2 is undefined for one test example. CSV cannot contain worksheets: observations.csv uses execution, seed, test_size, id and split columns, while observations.xlsx stores separate sheets. This preserves exact changing membership.',
'The legacy file store is recorded in store_contents.txt. Experiment metadata is in meta.yaml; each run has params, metrics, tags and artifact files. Server-backed later labs instead use SQLite metadata. Raw stores are excluded from Git.',
'Both baseline and delivery runs use the same HTTP tracking URI. Experiments group runs. A run records one execution. Parameters are settings, metrics numeric outcomes, tags descriptive metadata, artifacts files, and logged models reloadable packages. Start command is in README.md.',
'The exact twenty-patient table is used. Sixteen training and four test observations are logged, with actual hospital days, predicted days, signed prediction-minus-actual error and absolute error. The model is an educational illustration only.',
'Nine seed/split runs compare sizes 0.2, 0.3 and 0.4 within fixed seeds 7, 21 and 42. Training size does not monotonically determine error because test composition also changes. Counts, MAE and R2 are logged.',
'Same configuration and data are used under one experiment. Autologging captures estimator parameters, training metrics and a model. Manual logging explicitly captures held-out metrics, split settings, counts and the model. comparison.json records the actual differences.',
'The two separate client scripts use http://127.0.0.1:5000 and Lab07-Shared-Server. They differ by fit_intercept. They need no separate tracking servers and can log to the same experiment. Shared tracking centralizes provenance, results and artifacts for a team.',
'The sklearn model is logged, its URI saved, then loaded through mlflow.pyfunc and used on x=2,6,12. The inference path uses the stored package rather than training another model.',
'evaluate.py logs a custom SentimentModel PythonModel. The supplied wrapper bundles tokenizer and weights, and load_context restores the pipeline internally. Lab09 reads its recorded MLflow URI and predicts two new inputs through MLflow.',
'The first exact-named experiment logs parameters and MAE. The second also logs MSE and R2. MAE/MSE are lower-is-better; R2 is higher-is-better and can be negative. Metrics use only held-out rows.',
'Intercept and no-intercept model versions are registered under lab-regression. The lower-MAE version receives champion and the other challenger. Prediction resolves models:/lab-regression@champion and prints the version.',
'The original brief labels Projects as a second Lab11; it is recorded as Lab12. MLproject declares float test_size and integer random_state parameters. The unchanged train.py is invoked twice with 0.25/0.40 and seed7. MLflow Projects creates the enclosing run; the entry point resumes that run.',
'MlflowClient queries Lab05-Comparison with FINISHED status, ascending metrics.mae and max_results=3. The three lowest-MAE runs are saved in top_three.csv. Sharing the URI eliminates copying live databases.',
'Actual CLI version, help and experiment search commands were executed. Their complete output is in terminal.txt. The active tracking store is the same HTTP server used for the later labs.'
];
for(let i=1;i<=14;i++) {
 page(); heading(`Lab ${String(i).padStart(2,'0')} ${topics[i-1]}`);
 para('Code and command',{heading:HeadingLevel.HEADING_2});
 code(`.venv\\Scripts\\python.exe run_labs.py --lab ${i}`);
 para(`Implementation: run_labs.py, branch number == ${i}. Additional project/client files are in labs/.`);
 para('Observation and answer',{heading:HeadingLevel.HEADING_2}); para(observations[i-1]);
 const rel=`outputs/labs/lab_${String(i).padStart(2,'0')}/terminal.txt`;
 const raw = text(rel).split(/\r?\n/).filter(x=> !x.includes('View run') && !x.includes('View experiment'));
 para('Measured output excerpt',{heading:HeadingLevel.HEADING_2});
 code(raw.slice(0,28).map(x=>x.length>100?x.slice(0,97)+'...':x).join('\n'));
 if(raw.length>28) para(`Full output (${raw.length} lines): ${rel}. Excerpt shortened only for page readability.`);
}
for (const day of [1,2]) {
 page(); heading(`Day ${day} Quiz Answers`);
 para(quizzes.declaration);
 for (const [number, answer, explanation] of quizzes[`day_${day}`]) para(`${number}. ${answer} — ${explanation}`);
}
page();heading('Reproduction and Submission');
para('Follow README.md to install dependencies, start the tracking server, evaluate both models, register aliases, predict new examples and execute the labs. requirements-lock.txt records the executed package versions. Git history records the pre-run rule and subsequent implementation/evidence commits.');
para('Student identity is recorded in student.json. Course title and course code await student confirmation. Review all source and results for viva preparation. The GitHub repository uses the required USN name. If private, add the instructor before submitting its link to the LMS. Check submission_status.json for the current submission state.');
const doc = new Document({creator:'MLflow Skill Lab',title:'MLflow Skill Lab Completed Record',
 styles:{default:{document:{run:{font:'Calibri',size:22},paragraph:{spacing:{after:120}}}}},
 sections:[{properties:{page:{margin:{top:850,bottom:850,left:850,right:850}}},
 footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.RIGHT,children:[new TextRun('MLflow Skill Lab | '),new TextRun({children:[PageNumber.CURRENT]})]})]})},children}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync(path.join(root,'Completed_Lab_Record.docx'),b));
const quizChildren = [];
for (const day of [1,2]) {
 if(day === 2) quizChildren.push(new Paragraph({children:[new PageBreak()]}));
 quizChildren.push(new Paragraph({text:`MLOps with MLflow Day ${day} Quiz Answers`,heading:HeadingLevel.TITLE}));
 quizChildren.push(new Paragraph(`${student.name} | ${student.usn} | Section ${student.section}`));
 quizChildren.push(new Paragraph({text:quizzes.declaration,spacing:{after:200}}));
 for(const [number,answer,explanation] of quizzes[`day_${day}`]) quizChildren.push(new Paragraph({text:`${number}. ${answer} — ${explanation}`,spacing:{after:140}}));
}
const quizDoc = new Document({creator:student.name,title:'Completed MLOps Quiz Answers',styles:{default:{document:{run:{font:'Calibri',size:22}}}},sections:[{properties:{page:{margin:{top:850,bottom:850,left:850,right:850}}},children:quizChildren}]});
Packer.toBuffer(quizDoc).then(b=>fs.writeFileSync(path.join(root,'Completed_Quiz_Answers.docx'),b));
