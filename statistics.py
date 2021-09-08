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

def plot_histogram(X: list, freq: list):
    pass

def plot_scatter():
    pass

def plot_box():
    pass

def plot_bar():
    pass

def plot_corr():
    pass

def z_test():
    pass

def t_test():
    pass

# TODO: Generate LUT for statistical tests