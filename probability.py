# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 07:50:21 2021

@author: Gabriel
"""
from utils import C, integral 
import numpy as np

# Basic concepts

class SampleSpace:
    '''
    Defines a sample space for an arbitrary random experiment.
    
    It is expected that strings or numbers as well as tuples of those are used to define the elements of the set.
    '''
    def __init__(self, data: set):
        self.elements = data
        self.cardinality = len(self.elements)
    
    def __repr__(self):
        return f"{self.elements}"
    
class Event:
    '''
    Defines a subset of a sample space.
    
    '''
    def __init__(self, data: set, sample_space: SampleSpace):
        self.elements = data
        self.cardinality = len(self.elements)
        assert self.isSubset(sample_space), "The event must be a subset of the sample space."
        self.sample_space = sample_space
        
    def isSubset(self, Omega: SampleSpace) -> bool:
        return all([i in Omega.elements for i in self.elements])

def prob(event: Event) -> float:
    '''
    P(E) = NFC(E) / NCT(S)
    where,
     - NFC : Number of favorable cases to event E
     - TNC : Cardinality of the sample space S

    Parameters
    ----------
    event : Event

    Returns
    -------
    float
        P(E).

    '''
    return event.cardinality / event.sample_space.cardinality
    
def probGiven(A: Event, B: Event) -> float:
    '''
    P(A|B) = NCF(A) / NCF(B)
    where,
     - NFC : Number of favorable cases to the event
     
    Parameters
    ----------
    A : Event
    
    B : Event
        

    Returns
    -------
    float
        P(A|B).

    '''
    assert B.isSubset(A.sample_space), "The events must be from the same sample space"
    return A.cardinality / B.cardinality 

def probOr(A: Event, B: Event) -> float:
    '''
    P(A or B) = P(A) + P(B) - P(A and B)

    Parameters
    ----------
    A : Event
        
    B : Event
        

    Returns
    -------
    float
        P(A or B).

    '''
    return np.round(prob(A) + prob(B) - probAnd(A, B), 4)

def probAnd(A: Event, B: Event) -> float:
    '''
    P(A and B) = P(A)P(B|A) = P(B)P(A|B)

    Parameters
    ----------
    A : Event
        
    B : Event
        

    Returns
    -------
    float
        P(A and B).

    '''
    return np.round(prob(B) * probGiven(A, B), 4)

def checkDisjointUnion(P: list) -> bool:
    '''
    Returns True if the sets are a disjoint union (partition of a bigger set).

    Parameters
    ----------
    P : list
        List of events.

    Returns
    -------
    bool
        Is disjoint union

    '''
    sum1 = sum([len(E) for E in P])
    union = P[0]
    for i in range(1, len(P)):
        union = union.union(P[i])
    return sum1 == len(union)            
            
# Probability distributions

class DiscreteDistribution:
    '''
    Contains the implementation of the most relevant discrete distributions.
    
    Each one can be called returning the probability of assuming value x,
    each one has the mean, variance (var), skewness (sk) and kurtosis (kts) available.
    A cdf method is also available and calculate F(X <= x).
    '''
    
    class Bernoulli:
        '''
        Bernoulli distribution.
        
        Distribution for a binary random value with a given probability of success p.
        '''
        def __init__(self, p: float):
            assert 0 <= p <= 1, "Probability of success must be between 0 and 1"
            self.p = p 
            self.q = 1 - self.p
            self.mean = self.p
            self.var = self.p * self.q
            
        def __repr__(self):
            return f"Bernoulli with probability {self.p} \nmean = {self.mean} and variance = {self.var}"
        
        def __call__(self, x: int) -> float:
            if not(x in (0, 1)):
                raise Exception("Invalid outcome for a bernoulli trial (x must be binary)")
            return self.p**x * self.q**(1 - x)
        
        def cdf(self, x: int) -> float:
            if x < 0:
                return 0
            elif x >= 1:
                return 1
            else:
                return self.q
        
    class Binomial:
        '''
        Binomial Distribution
        
        Distribuition for n trials of Bernoulli experiment with probability of success p
        '''
        def __init__(self, n: int, p: float):
            assert 0 <= p <= 1, "Probability of success must be between 0 and 1"
            self.n = n
            self.p = p 
            self.q = 1 - self.p
            self.mean = np.round(self.n * self.p, 4)
            self.var = np.round(self.n * self.p * self.q, 4)
            
        def __repr__(self):
            return f"Binomial with {self.n} number of trials and probability {self.p} \
                     \nmean = {self.mean} and variance = {self.var}"
        
        def __call__(self, x: int) -> float:
            if not(x in range(self.n+1)):
                raise Exception(f"x must be in [0, {self.n}] range")
            return np.round(C(self.n, x) * self.p**x * self.q**(self.n-x), 4)
        
        def cdf(self, x: int) -> float:
            if x < 0:
                return 0
            elif x >= self.n:
                return 1
            else:
                f = lambda t: (t**(self.n - x - 1)) * (1 - t)**x
                return np.round((self.n - x) * C(self.n, x) * integral(f, 0, self.q), 4)
    
    class Geometric:
        '''
        Geometric Distribution
        
        Distribution for number consecutive trials to get the first success
        '''
        def __init__(self, p: float):
            assert 0 <= p <= 1, "Probability of success must be between 0 and 1"
            self.p = p 
            self.q = 1 - self.p
            self.mean = np.round(self.q / self.p, 4)
            self.var = np.round(self.mean / self.p, 4)
            
        def __repr__(self):
            return f"Geometric with a success probability {self.p} \
                     \nmean = {self.mean} and variance = {self.var}"
        
        def __call__(self, x: int) -> float:
            if not(x >= 0):
                raise Exception("x must be greater or equal to 0")
            return np.round(self.p * (self.q**x), 4)
        
        def cdf(self, x: int) -> float:
            if x < 0:
                return 0
            else:
                return np.round(1 - self.q**(x + 1), 4)