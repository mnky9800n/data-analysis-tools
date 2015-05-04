import numpy as np

def add_jitter(df, jitter):
    """
    Adds jitter to a data set based on a random normal
    distribution.
    
    Requirements: numpy, pandas
    """
    return abs(df + np.random.normal(df, jitter, size=len(df)))

