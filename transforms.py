import random
import numpy as np

class RandomHorizontalFlip3D(object):
    
    def __init__(self, p=0.5):
        self.p = p
        
    def __call__(self, sample):
        if random.random() < self.p:
            return np.flip(sample, axis=2).copy()
        else: return sample
        
class RandomVerticalFlip3D(object):
    
    def __init__(self, p=0.5):
        self.p = p
        
    def __call__(self, sample):
        if random.random() < self.p:
            return np.flip(sample, axis=3).copy()
        else: return sample
        
class RandomHorizontalFlip2D(object):
    
    def __init__(self, p=0.5):
        self.p = p
        
    def __call__(self, sample):
        if random.random() < self.p:
            return np.flip(sample, axis=1).copy()
        else: return sample
        
class RandomVerticalFlip2D(object):
    
    def __init__(self, p=0.5):
        self.p = p
        
    def __call__(self, sample):
        if random.random() < self.p:
            return np.flip(sample, axis=2).copy()
        else: return sample