from utils import floor

def mean(X: list) -> float:
    return sum(X) / len(X)

def mode(X: list) -> float:
    return max(set(X), key=list(X).count)

def median(X: list) -> float:
    X_sorted = sorted(X)
    n = len(X)
    if n % 2 != 0:
        return X_sorted[(n - 1) // 2]
    return (X_sorted[(n - 1) // 2] + X_sorted[((n - 1) // 2) + 1]) / 2

def variance(X: list) -> float:
    return sum([(x - mean(X))**2 for x in X]) / (len(X) - 1)

def std(X: list) -> float:
    return variance(X)**0.5

def plotHistogram(X: list, freq: list):
    pass

def plotScatter():
    pass

def plotBox():
    pass

def plotBar():
    pass

def plotCorr():
    pass

def confidenceIntMean():
    pass

def confidenceIntProportion():
    pass

def confidenceInt2Means():
    pass

def zTest():
    pass

def tTest():
    pass

# TODO: Generate LUT for statistical tests