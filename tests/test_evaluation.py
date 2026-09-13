import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from apg_ams.evaluation import dataset_catalog, UCI_DATASETS

def test_catalog_contains_original_benchmarks_without_network():
    names=set(dataset_catalog(include_uci=False))
    required={"Iris","Wine","BreastCancer","Digits","Synthetic20D","Synthetic50D","TwoMoons","ConcentricCircles"}
    assert required.issubset(names)

def test_revision_uci_dataset_ids_are_frozen():
    assert UCI_DATASETS=={"Ionosphere":52,"Sonar":151,"Banknote":267,"MiceProtein":342}
