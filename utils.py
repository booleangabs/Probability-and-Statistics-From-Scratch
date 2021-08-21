# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:35:05 2021

@author: Gabriel
"""
def floor(x: float) -> int:
    return int(x)

def ceil(x: float) -> int:
    return int(x) + 1

def frac(x: float) -> int:
    return x - int(x)

def fact(n: int) -> int:
    '''
    Return the factorial of a number

    Parameters
    ----------
    n : int
        Integer.

    Returns
    -------
    int
        Factorial of n.

    '''
    
    return 1 if n == 0 else n * fact(n-1)

def C(n: int, r: int) -> int:
    '''
    Number of combinations of n things taken r at a time

    Parameters
    ----------
    n : int
        DESCRIPTION.
    r : int
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    '''
    
    assert n >= r, "n must be greater or equal than r"
    
    return fact(n) // (fact(r) * fact(n-r))

def P(n: int, r: int) -> int:
    '''
    Number of combinations of n things taken r at a time

    Parameters
    ----------
    n : int
        DESCRIPTION.
    r : int
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    '''
    assert n >= r, "n must be greater or equal than r"
    
    return fact(n) // fact(n-r)

def summation(f, a: int, b: int) -> float:
    '''
    Cummulative sum of f.

    Parameters
    ----------
    f : function
        A numerical function.
    a : int
        Summation lower bound.
    b : int
        Summation upper bound.

    Returns
    -------
    float
        Cummulative value of f in the interval specified.

    '''
    
    s = 0
    for i in range(a, b):
        s += f(i)
    
    return s

def integral(f, a: float, b: float, n: int = 1000) -> float:
    '''
    Integral of f.

    Parameters
    ----------
    f : function
        A numerical function.
    a : float
        Integral lower bound.
    b : float
        Integral upper bound.
    n : int
        Number of subdivisions of the interval.

    Returns
    -------
    float
        Integral of f from a to b.

    '''
    
    dx = (b - a) / n
    F = 0
    x = a
    for i in range(n + 1):
        F += f(x) * dx
        x += dx
        
    return F



    