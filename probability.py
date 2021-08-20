# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 07:50:21 2021

@author: Gabriel
"""

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
    
    def prob(self):
        return self.cardinality / self.sample_space.cardinality
    
    
class DiscreteDistribution:
    def __init__(self):
        pass
    
    class bernoulli:
        def __init__(self, p: float):
            self.p = p 
            self.q = 1 - self.p
            self.mean = self.p
            self.var = self.p * self.q
            
        def __repr__(self):
            return f"Bernoulli with mean = {self.mean} and variance = {self.var}"
        
        def __call__(self, x: float) -> float:
            if not(x in (0, 1)):
                return 0
            return self.p**x * self.q**(1-x)
            
    
        