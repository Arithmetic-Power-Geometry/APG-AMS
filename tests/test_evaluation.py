import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from apg_ams.evaluation import dataset_catalog

def test_catalog_contains_original_benchmarks():
    names=set(dataset_catalog())
    required={"Iris","Wine","BreastCancer","Digits","Synthetic20D","Synthetic50D","TwoMoons","ConcentricCircles"}
    assert required.issubset(names)
