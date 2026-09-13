import time
import warnings
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, load_digits, make_classification, make_moons, make_circles
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.preprocessing import StandardScaler
from .core import apg_ams_predict_one, full_p_search_predict_one, P_GRID

# Four additional importable real-world UCI classification datasets.
UCI_DATASETS={"Ionosphere":52,"Sonar":151,"Banknote":267,"MiceProtein":342}

def _clean_xy(X,y):
    """Coerce features/target without fitting any data-dependent transform.

    Missing-value imputation is deliberately deferred to each training fold in
    _scale() to prevent train-test leakage.
    """
    X=pd.DataFrame(X).apply(pd.to_numeric,errors="coerce").dropna(axis=1,how="all")
    y=pd.DataFrame(y).iloc[:,0]
    mask=~pd.isna(y)
    X=X.loc[mask].reset_index(drop=True); y=y.loc[mask].astype(str).reset_index(drop=True)
    return X.to_numpy(dtype=float),np.asarray(y)

def dataset_catalog(include_uci=True,random_state=42):
    ds={}
    for name,loader in [("Iris",load_iris),("Wine",load_wine),("BreastCancer",load_breast_cancer),("Digits",load_digits)]:
        b=loader(); ds[name]=(b.data.astype(float),b.target.astype(str))
    X,y=make_classification(n_samples=1000,n_features=20,n_informative=8,n_redundant=4,random_state=random_state); ds["Synthetic20D"]=(X,y.astype(str))
    X,y=make_classification(n_samples=1000,n_features=50,n_informative=12,n_redundant=8,random_state=random_state); ds["Synthetic50D"]=(X,y.astype(str))
    X,y=make_moons(n_samples=1000,noise=.2,random_state=random_state); ds["TwoMoons"]=(X,y.astype(str))
    X,y=make_circles(n_samples=1000,noise=.08,factor=.5,random_state=random_state); ds["ConcentricCircles"]=(X,y.astype(str))
    if include_uci:
        from ucimlrepo import fetch_ucirepo
        for name,uid in UCI_DATASETS.items():
            obj=fetch_ucirepo(id=uid); ds[name]=_clean_xy(obj.data.features,obj.data.targets)
    return ds

def _scale(Xtr,Xte):
    # Fold-safe preprocessing: all fitted transforms see training data only.
    imp=SimpleImputer(strategy="median").fit(Xtr); Xtr=imp.transform(Xtr); Xte=imp.transform(Xte)
    sc=StandardScaler().fit(Xtr); return sc.transform(Xtr),sc.transform(Xte)

def _eval_fold(Xtr,Xte,ytr,yte,tau=.92,k=7,random_state=42,run_lmnn=True):
    Xtr,Xte=_scale(Xtr,Xte); out={}
    t=time.perf_counter(); clf=KNeighborsClassifier(n_neighbors=k,p=2).fit(Xtr,ytr); pred=clf.predict(Xte)
    out["L2"]=(accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,np.nan)
    t=time.perf_counter(); pred=[full_p_search_predict_one(Xtr,ytr,x,k=k)[0] for x in Xte]
    out["FullP"]=(accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,0.0)
    t=time.perf_counter(); pred=[]; costs=[]
    for x in Xte:
        pr,_,_,c=apg_ams_predict_one(Xtr,ytr,x,tau=tau,k=k); pred.append(pr); costs.append(c)
    red=100*(1-np.sum(costs)/(len(costs)*len(P_GRID)))
    out["APG_AMS"]=(accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,red)
    t=time.perf_counter(); nca=NeighborhoodComponentsAnalysis(random_state=random_state,max_iter=100); Xn=nca.fit_transform(Xtr,ytr); Xt=nca.transform(Xte)
    pred=KNeighborsClassifier(n_neighbors=k).fit(Xn,ytr).predict(Xt)
    out["NCA"]=(accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,np.nan)
    if run_lmnn:
        from metric_learn import LMNN
        t=time.perf_counter(); minc=int(np.min(np.unique(ytr,return_counts=True)[1])); lk=min(k,max(1,minc-1))
        lmnn=LMNN(k=lk,max_iter=100,convergence_tol=1e-6)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore"); lmnn.fit(Xtr,ytr)
        Xl=lmnn.transform(Xtr); Xlt=lmnn.transform(Xte); pred=KNeighborsClassifier(n_neighbors=k).fit(Xl,ytr).predict(Xlt)
        out["LMNN"]=(accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,np.nan)
    return out

def evaluate_all(n_splits=10,tau=.92,k=7,random_state=42,include_uci=True,run_lmnn=True):
    rows=[]
    for dname,(X,y) in dataset_catalog(include_uci,random_state).items():
        cv=StratifiedKFold(n_splits=n_splits,shuffle=True,random_state=random_state)
        for fold,(tr,te) in enumerate(cv.split(X,y),1):
            out=_eval_fold(X[tr],X[te],y[tr],y[te],tau,k,random_state,run_lmnn)
            for method,(acc,f1,rt,red) in out.items():
                rows.append(dict(dataset=dname,fold=fold,method=method,accuracy=acc,weighted_f1=f1,runtime_seconds=rt,search_reduction_percent=red,n_samples=len(X),n_features=X.shape[1]))
    return pd.DataFrame(rows)
