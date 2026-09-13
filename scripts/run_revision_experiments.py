from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np, pandas as pd
from scipy.stats import ttest_rel, wilcoxon
from apg_ams.evaluation import evaluate_all

OUT=Path("results"); OUT.mkdir(exist_ok=True)
df=evaluate_all(n_splits=10,tau=.92,k=7,include_uci=True,run_lmnn=True)
df.to_csv(OUT/"fold_results.csv",index=False)
summary=(df.groupby(["dataset","method","n_samples","n_features"],as_index=False)
           .agg(accuracy_mean=("accuracy","mean"),accuracy_sd=("accuracy","std"),
                weighted_f1_mean=("weighted_f1","mean"),weighted_f1_sd=("weighted_f1","std"),
                runtime_mean_seconds=("runtime_seconds","mean"),
                search_reduction_mean_percent=("search_reduction_percent","mean")))
summary.to_csv(OUT/"benchmark_summary.csv",index=False)
rows=[]
apg=df[df.method=="APG_AMS"].set_index(["dataset","fold"])
for m in ["L2","FullP","NCA","LMNN"]:
    other=df[df.method==m].set_index(["dataset","fold"])
    common=apg.index.intersection(other.index)
    for metric in ["accuracy","weighted_f1"]:
        a=apg.loc[common,metric].astype(float).values; b=other.loc[common,metric].astype(float).values
        t=ttest_rel(a,b,nan_policy="omit")
        try: wp=float(wilcoxon(a,b,zero_method="zsplit").pvalue)
        except Exception: wp=float("nan")
        rows.append(dict(comparison=f"APG_AMS vs {m}",metric=metric,n_pairs=len(common),
                         mean_apg=float(np.mean(a)),mean_other=float(np.mean(b)),
                         mean_difference=float(np.mean(a-b)),paired_t_p=float(t.pvalue),wilcoxon_p=wp))
pd.DataFrame(rows).to_csv(OUT/"paired_statistics.csv",index=False)
print(summary.to_string(index=False))
print(pd.DataFrame(rows).to_string(index=False))
