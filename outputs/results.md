|Metric|A|B|B minus A|
|---|---:|---:|---:|
|accuracy|0.966667|0.800000|-0.166667|
|macro_precision|0.968750|0.837500|-0.131250|
|macro_recall|0.966667|0.800000|-0.166667|
|macro_f1|0.966630|0.794286|-0.172344|
|avg_latency_ms|8.623835|0.870680|-7.753155|
|total_inference_s|0.517430|0.052241|-0.465189|
|parameters_millions|66.955010|4.386178|-62.568832|

Model A is the Champion under the rule declared before evaluation. The Challenger's macro-F1 is 0.7943, compared with 0.9666 for A: a difference of -17.23 percentage points. The required improvement is one percentage point and the measured latency ratio B/A is 0.101. Promotion requires both conditions; a speed advantage alone does not justify replacement under this policy. The comparison uses the same sixty sentences in the same order, with thirty intended labels in each class. With only sixty observations, a single changed prediction can move accuracy by about 1.67 percentage points. Consequently the observed difference should not be interpreted as proof of a population-level improvement or statistical significance. Macro-F1 gives both classes equal weight, while the confusion matrices show which class accounts for errors. The tiny model uses fewer parameters and may be useful where memory and CPU throughput matter more than this accuracy policy. The disagreement table records all observed conflicting predictions for qualitative review. Before deployment, the decision should be checked on a larger independently labeled sample drawn from actual users, including ambiguous language and domain shifts.