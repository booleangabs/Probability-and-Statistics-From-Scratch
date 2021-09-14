from utils import floor
import matplotlib.pyplot as plt
from data import DataCsv, TimeSeries

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

def plotHistogram(X: DataCsv, name: str):
    data = X[name]
    sorted(data)
    x1 = data[:len(data) // 2]
    x2 = data[len(data) // 2:]
    IQR = (median(x2) - median(x1))
    h = 2 * IQR / (len(data)**(1 / 3))
    n = (max(data) - min(data)) // h
    plt.hist(data, bins = int(n))
    plt.show()
    
def plotScatter(X: list, Y: list):
    plt.scatter(X, Y)
    plt.show()

def plotBox(X: list, Y: list):
    pass

def plotBar(X: list, Y: list):
    pass

def plotCorr(X: list, Y: list):
    pass

def confidenceIntMean(sample_mean: float, mean: float, std: float, alpha: float= 0.95, from_pop: bool= False):
    pass

def confidenceIntProportion(previous_belief: float, test_prop: float):
    pass

def confidenceInt2Means():
    pass

def zTest():
    pass

def tTest():
    pass

# TODO: Generate LUT for statistical tests