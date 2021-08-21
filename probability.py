# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 07:50:21 2021

@author: Gabriel
"""
from utils import C, summation, integral, floor, ceil

class SampleSpace:
    def __init__(self, data: set):
        self.elements = data
        self.cardinality = len(self.elements)
    
    def __repr__(self):
        return f"{self.elements}"
    
class Event:
    def __init__(self, data: set, sample_space: SampleSpace):
        self.elements = data
        self.cardinality = len(self.elements)
        assert self.isSubset(sample_space), "The event must be a subset of the sample space."
        self.sample_space = sample_space
        
    def isSubset(self, Omega: SampleSpace):
        return all([i in Omega.elements for i in self.elements])
    
class DiscreteDistribution:
    def __init__(self):
        pass
    
    class bernoulli:
        def __init__(self, p: float):
            assert 0 <= p <= 1, "Probability of success must be between 0 and 1"
            self.p = p 
            self.q = 1 - self.p
            self.mean = self.p
            self.var = self.p * self.q
            
        def __repr__(self):
            return f"Bernoulli with probability {self.p} \nmean = {self.mean} and variance = {self.var}"
        
        def __call__(self, x: int) -> int:
            if not(x in (0, 1)):
                return 0
            return self.p**x * self.q**(1-x)
        
        def cdf(self, x: int) -> int:
            if x < 0:
                return 0
            elif x > 1:
                return 1
            else:
                return self.q
        
    class binomial:
        def __init__(self, n: int, p: float):
            assert 0 <= p <= 1, "Probability of success must be between 0 and 1"
            self.n = n
            self.p = p 
            self.q = 1 - self.p
            self.mean = self.n * self.p
            self.var = self.n * self.p * self.q
            
        def __repr__(self):
            return f"Binomial with {self.n} number of trials and probability {self.p} \nmean = {self.mean} and variance = {self.var}"
        
        def __call__(self, x: int) -> int:
            if not(x in range(self.n+1)):
                return 0
            return C(self.n, x) * self.p**x * self.q**(self.n-x)
        
        def cdf(self, x: int) -> float:
            if x < 0:
                return 0
            elif x > self.n:
                return 1
            else:
                f = lambda t: (t**(self.n - x - 1)) * (1-t)**x
                return (self.n - x)*C(self.n, x)*integral(f, 0, self.q)
            
        
def prob(event: Event) -> float:
    return event.cardinality / event.sample_space.cardinality
    
def prob_given(A: Event, B: Event) -> float:
    assert B.isSubset(A.sample_space), "The events must be from the same sample space"
    return A.cardinality / B.cardinality 

def prob_or(A: Event, B: Event) -> float:
    return prob(A) + prob(B) - prob_and(A, B)

def prob_and(A: Event, B: Event) -> float:    
    return prob(B) * prob_given(A, B)
    
        