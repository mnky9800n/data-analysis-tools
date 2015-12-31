def MAD(data : np.array):
  """
  returns the median absolute deviation of a distribution
  
  useful for non-normal distributions, etc.
  """
  return np.median(abs(data - np.median(data)))
