import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import numpy as np
from apg_ams.core import normalized_apg_entropy, apg_ams_predict_one, full_p_search_predict_one

def test_entropy_range():
    for x in [np.array([1.,2.,3.]), np.array([1.,1.,1.]), np.array([-2.,0.,5.])]:
        h = normalized_apg_entropy(x)
        assert 0.0 <= h <= 1.0 + 1e-12

def test_single_dimension_entropy():
    assert normalized_apg_entropy(np.array([3.0])) == 0.0

def test_predictions_are_valid_labels():
    X=np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.],[2.,2.],[2.,1.],[1.,2.]])
    y=np.array([0,0,0,1,1,1,1])
    pred,p=full_p_search_predict_one(X,y,np.array([1.2,1.2]),k=3)
    assert pred in set(y)
    assert p in {1.0,1.5,2.0,3.0,4.0}
    pred,p,h,cost=apg_ams_predict_one(X,y,np.array([1.2,1.2]),tau=.92,k=3)
    assert pred in set(y)
    assert cost in {1,5}
