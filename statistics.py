import matplotlib.pyplot as plt
import seaborn as sns
from data import DataCsv
import numpy as np

def mean(X: list) -> float:
    '''
    Computes the mean of a list

    Parameters
    ----------
    X : list
        

    Returns
    -------
    float
        Mean of X.

    '''
    return np.round(sum(X) / len(X), 4)

def mode(X: list) -> float:
    '''
    Computes the mode of a list

    Parameters
    ----------
    X : list
        

    Returns
    -------
    Mode of X.

    '''
    return max(set(X), key=list(X).count)

def modeWithFrequency(X: list, f: list) :
    '''
    Computes the mode of a list based of frequency values

    Parameters
    ----------
    X : list
        List of values.
    f : list
        The respective frequencies.

    Returns
    -------
    Mode of X.

    '''
    return X[f.index(max(f))]

def median(X: list) -> float:
    '''
    Computes the median of X.

    Parameters
    ----------
    X : list
        

    Returns
    -------
    float
        Median of X.

    '''
    X_sorted = sorted(X)
    n = len(X)
    if n % 2 != 0:
        return X_sorted[(n - 1) // 2]
    return (X_sorted[(n - 1) // 2] + X_sorted[((n - 1) // 2) + 1]) / 2

def variance(X: list) -> float:
    '''
    Computes variance of X (sample variance).

    Parameters
    ----------
    X : list

    Returns
    -------
    float
        Variance of X.

    '''
    return np.round(sum([(x - mean(X))**2 for x in X]) / (len(X) - 1), 4)

def std(X: list) -> float:
    '''
    Computes standard deviation of X (sample std).

    Parameters
    ----------
    X : list
        DESCRIPTION.

    Returns
    -------
    float
        Standard deviation of X.

    '''
    return np.round(variance(X)**0.5, 4)

def cov(X: list, Y: list) -> float:
    '''
    Computes the covariance of X and Y.

    Parameters
    ----------
    X : list
        
    Y : list
        

    Returns
    -------
    float
        Covariance of X and Y.

    '''
    mx, my = mean(X), mean(Y)
    return np.round(sum([(i - mx) * (j - my) for i, j in zip(X, Y)]) / (len(X) - 1), 4)

def corr(X: list, Y: list) -> float:
    '''
    Computes the correlation of X and Y.

    Parameters
    ----------
    X : list
        
    Y : list
        

    Returns
    -------
    float
        Correlation of X and Y.

    '''
    stdx, stdy = std(X), std(Y)
    covxy = cov(X, Y)
    return np.round(covxy / (stdx * stdy), 4)

def plotHistogram(X: DataCsv, name: str):
    '''
    Plots histogram of column "name"

    Parameters
    ----------
    X : DataCsv
        The dataset.
    name : str
        The column.

    Returns
    -------
    None.

    '''
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
    '''
    Plots scatterplot of X and Y.

    Parameters
    ----------
    X : list
        
    Y : list
        
    title : str, optional
        Title for the plot. The default is None.
    labels : list, optional
        Labels for the x and y axis. The default is None.

    Returns
    -------
    None.

    '''
    if title:
        figure, axis = plt.subplots()
        axis.set_title(title)
    if labels:
        axis.set_xlabel(labels[0])
        axis.set_ylabel(labels[1])
    plt.scatter(X, Y)
    plt.show()

def plotBox(X: list, title: str= None):
    '''
    Plots box plot of X.

    Parameters
    ----------
    X : list
        
    title : str, optional
        Title for the plot. The default is None.

    Returns
    -------
    None.

    '''
    if title:
        figure, axis = plt.subplots()
        axis.set_title(title)
    plt.boxplot(X)
    plt.show()

def plotBar(X: list, Y: list, title: str= None):
    '''
    Plots bar plot using X and Y.

    Parameters
    ----------
    X : list
        The classes.
    Y : list
        The heights.
    title : str, optional
        Title for the plot. The default is None.

    Returns
    -------
    None.

    '''
    if title:
        figure, axis = plt.subplots()
        axis.set_title(title)
    plt.bar(X, Y)
    plt.show()

def plotCorr(data: DataCsv):
    '''
    Plots correlation matrix for the dataset

    Parameters
    ----------
    data : DataCsv
        

    Returns
    -------
    None.

    '''
    corr_matrix = [[corr(data[i], data[j]) for i in data.header] for j in data.header]
    sns.heatmap(corr_matrix, annot=True, xticklabels=data.header, yticklabels=data.header)
    
def confidenceIntMeanZ(sample_mean: float, n: int, std: float, CL: float= 0.95) -> tuple:
    '''
    Calculates 0.9, 0.95 or 0.99 confidence interval for the sample mean.

    Parameters
    ----------
    sample_mean : float
        
    n : int
        Number of observations.
    std : float
        Population standard deviation.
    CL : float, optional
        Confidence level. The default is 0.95.

    Returns
    -------
    tuple
        Margin of error and interval limits.

    '''
    margin = z_score(CL) * (std / (np.sqrt(n)))
    return margin, [sample_mean - margin, sample_mean + margin]

def z_score(CL: float) -> float:
    '''
    

    Parameters
    ----------
    CL : float
        Confidence level.

    Raises
    ------
    Exception
        When CL has an unexpected value.

    Returns
    -------
    float
        Z score for the given CL.

    '''
    cls_ = {0.90: 1.645, 0.95: 1.96, 0.99: 2.58}
    if not CL in cls_:
        raise Exception("Use one of the following for C.L.: 0.9, 0.95, 0.99")
    return cls_[CL]

def confidenceIntProportion(p: float, n: int, CL: float) -> tuple:
    '''
    Calculates 0.9, 0.95 or 0.99 confidence interval for the sample proportion.

    Parameters
    ----------
    p : float
        Sample proportion.
    n : int
        Number of observations.
    CL : float
        Confidence level.

    Returns
    -------
    tuple
        Margin of error and interval limits.

    '''
    margin = z_score(CL) * np.sqrt((p * (1- p))/ n)
    return margin, [p - margin, p + margin]
