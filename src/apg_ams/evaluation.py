import importlib.util
import time
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, load_digits, make_classification, make_moons, make_circles
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from apg_ams.core import apg_ams_predict_one, full_p_search_predict_one, P_GRID

def dataset_catalog(random_state=42):
    datasets = {}
    for name, loader in [("Iris", load_iris),("Wine", load_wine),("BreastCancer", load_breast_cancer),("Digits", load_digits)]:
        b = loader(); datasets[name] = (b.data.astype(float), b.target)
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=8, n_redundant=4, random_state=random_state); datasets["Synthetic20D"]=(X,y)
    X, y = make_classification(n_samples=1000, n_features=50, n_informative=12, n_redundant=8, random_state=random_state); datasets["Synthetic50D"]=(X,y)
    X, y = make_moons(n_samples=1000, noise=0.2, random_state=random_state); datasets["TwoMoons"]=(X,y)
    X, y = make_circles(n_samples=1000, noise=0.08, factor=0.5, random_state=random_state); datasets["ConcentricCircles"]=(X,y)
    return datasets

def evaluate_all(n_splits=10, tau=0.92, k=7, include_lmnn=False, random_state=42):
    rows=[]
    for dname,(X,y) in dataset_catalog(random_state).items():
        cv=StratifiedKFold(n_splits=n_splits,shuffle=True,random_state=random_state)
        for fold,(tr,te) in enumerate(cv.split(X,y),1):
            Xtr,Xte,ytr,yte=X[tr],X[te],y[tr],y[te]
            sc=StandardScaler().fit(Xtr); Xtrs=sc.transform(Xtr); Xtes=sc.transform(Xte)
            t=time.perf_counter(); m=KNeighborsClassifier(n_neighbors=k,p=2).fit(Xtrs,ytr); pred=m.predict(Xtes); rows.append([dname,fold,"L2",accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,np.nan])
            t=time.perf_counter(); pred=[full_p_search_predict_one(Xtrs,ytr,x,k=k)[0] for x in Xtes]; rows.append([dname,fold,"FullP",accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,0.0])
            t=time.perf_counter(); pred=[]; costs=[]
            for x in Xtes:
                yp,_,_,c=apg_ams_predict_one(Xtrs,ytr,x,tau=tau,k=k); pred.append(yp); costs.append(c)
            red=100*(1-np.sum(costs)/(len(costs)*len(P_GRID))); rows.append([dname,fold,"APG_AMS",accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,red])
            nca=Pipeline([("scale",StandardScaler()),("nca",NeighborhoodComponentsAnalysis(random_state=random_state,max_iter=100)),("knn",KNeighborsClassifier(n_neighbors=k,p=2))])
            t=time.perf_counter(); nca.fit(Xtr,ytr); pred=nca.predict(Xte); rows.append([dname,fold,"NCA",accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,np.nan])
            if include_lmnn and importlib.util.find_spec("metric_learn") is not None:
                from metric_learn import LMNN
                sc2=StandardScaler().fit(Xtr); a=sc2.transform(Xtr); b=sc2.transform(Xte)
                t=time.perf_counter(); lmnn=LMNN(k=k,learn_rate=1e-6,max_iter=100).fit(a,ytr); a=lmnn.transform(a); b=lmnn.transform(b); knn=KNeighborsClassifier(n_neighbors=k,p=2).fit(a,ytr); pred=knn.predict(b); rows.append([dname,fold,"LMNN",accuracy_score(yte,pred),f1_score(yte,pred,average="weighted"),time.perf_counter()-t,np.nan])
    return pd.DataFrame(rows,columns=["dataset","fold","method","accuracy","weighted_f1","runtime_seconds","search_reduction_percent"])
