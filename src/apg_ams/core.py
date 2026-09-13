import numpy as np

P_GRID = (1.0, 1.5, 2.0, 3.0, 4.0)

def _positive_map(x, eps=1e-12):
    x = np.asarray(x, dtype=float)
    lo = np.min(x)
    hi = np.max(x)
    if hi - lo < eps:
        return np.ones_like(x)
    return (x - lo) / (hi - lo) + eps

def normalized_apg_entropy(x, eps=1e-12):
    z = _positive_map(x, eps=eps)
    w = z ** 2
    s = w.sum()
    if s <= eps:
        return 0.0
    w = w / s
    d = w.size
    if d <= 1:
        return 0.0
    h = -np.sum(w * np.log(np.clip(w, eps, 1.0)))
    return float(h / np.log(d))

def minkowski_distances(X, x, p):
    X = np.asarray(X, dtype=float)
    x = np.asarray(x, dtype=float)
    return np.sum(np.abs(X - x) ** p, axis=1) ** (1.0 / p)

def _majority_vote(labels):
    values, counts = np.unique(labels, return_counts=True)
    return values[np.argmax(counts)]

def _predict_with_p(X_train, y_train, x, p, k):
    d = minkowski_distances(X_train, x, p)
    idx = np.argsort(d)[:k]
    return _majority_vote(y_train[idx]), y_train[idx]

def _local_purity(neighbor_labels):
    _, counts = np.unique(neighbor_labels, return_counts=True)
    return float(np.max(counts) / len(neighbor_labels))

def full_p_search_predict_one(X_train, y_train, x, k=7, p_grid=P_GRID):
    best = None
    for p in p_grid:
        pred, nbr_labels = _predict_with_p(X_train, y_train, x, p, k)
        purity = _local_purity(nbr_labels)
        candidate = (purity, -abs(p - 2.0), p, pred)
        if best is None or candidate > best:
            best = candidate
    return best[-1], float(best[-2])

def apg_ams_predict_one(X_train, y_train, x, tau=0.92, k=7, p_grid=P_GRID):
    h = normalized_apg_entropy(x)
    if h < tau:
        pred, _ = _predict_with_p(X_train, y_train, x, 2.0, k)
        return pred, 2.0, h, 1
    pred, p = full_p_search_predict_one(X_train, y_train, x, k=k, p_grid=p_grid)
    return pred, p, h, len(p_grid)
