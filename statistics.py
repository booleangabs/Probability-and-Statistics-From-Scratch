import matplotlib.pyplot as plt
import seaborn as sns
from data import DataCsv
import numpy as np

def mean(X: list) -> float:
    return np.round(sum(X) / len(X), 4)

def mode(X: list) -> float:
    return max(set(X), key=list(X).count)

def median(X: list) -> float:
    X_sorted = sorted(X)
    n = len(X)
    if n % 2 != 0:
        return X_sorted[(n - 1) // 2]
    return (X_sorted[(n - 1) // 2] + X_sorted[((n - 1) // 2) + 1]) / 2

def variance(X: list) -> float:
    return np.round(sum([(x - mean(X))**2 for x in X]) / (len(X) - 1), 4)

def std(X: list) -> float:
    return np.round(variance(X)**0.5, 4)

def cov(X: list, Y: list) -> float:
    mx, my = mean(X), mean(Y)
    return np.round(sum([(i - mx) * (j - my) for i, j in zip(X, Y)]) / (len(X) - 1), 4)

def corr(X: list, Y: list) -> float:
    stdx, stdy = std(X), std(Y)
    covxy = cov(X, Y)
    return np.round(covxy / (stdx * stdy), 4)

def plotHistogram(X: DataCsv, name: str):
    data = X[name]
    sorted(data)
    x1 = data[:len(data) // 2]
    x2 = data[len(data) // 2:]
    IQR = (median(x2) - median(x1))
    h = 2 * IQR / (len(data)**(1 / 3))
    n = (max(data) - min(data)) // h
    figure, axis = plt.subplots()
    axis.set_title(name)
    plt.hist(data, bins = int(n))
    plt.show()
    
def plotScatter(X: list, Y: list, title: str= None, labels: list= None):
    if title:
        figure, axis = plt.subplots()
        axis.set_title(title)
    if labels:
        axis.set_xlabel(labels[0])
        axis.set_ylabel(labels[1])
    plt.scatter(X, Y)
    plt.show()

def plotBox(X: list, title: str= None):
    if title:
        figure, axis = plt.subplots()
        axis.set_title(title)
    plt.boxplot(X)
    plt.show()

def plotBar(X: list, Y: list, title: str= None):
    if title:
        figure, axis = plt.subplots()
        axis.set_title(title)
    plt.bar(X, Y)
    plt.show()

def plotCorr(data: DataCsv):
    corr_matrix = [[corr(data[i], data[j]) for i in data.header] for j in data.header]
    sns.heatmap(corr_matrix, annot=True, xticklabels=data.header, yticklabels=data.header)
    
def confidenceIntMean(sample_mean: float, n: int, std: float, CL: float= 0.95) -> tuple:
    margin = z_score(CL) * (std / (np.sqrt(n)))
    return margin, [sample_mean - margin, sample_mean + margin]

def z_score(CL: float) -> float:
    cls_ = {0.90: 1.645, 0.95: 1.96, 0.99: 2.58}
    if not CL in cls_:
        raise Exception("Use one of the following for C.L.: 0.9, 0.95, 0.99")
    return cls_[CL]

def confidenceIntProportion(p: float, n: int, CL: float) -> tuple:
    margin = z_score(CL) * np.sqrt((p * (1- p))/ n)
    return margin, [p - margin, p + margin]

def zTest():
    pass

def tTest():
    pass

# TODO: Generate LUT for statistical tests