from matplotlib.pylab import pcolor

def make_correlation_matrix(df, title):
  """
  Creates a matplotlib plot of values (typically a correlation dataframe from Pandas).
  This plot has each value in a cell shaded on a color map for the entire
  matrix. The color map is by default reverse gray scale.
  """

  fig, ax = plt.subplots(figsize=(12,12))
  pcolor(df, cmap='gray_r')
  plt.title(title)
  for n,mc in enumerate(df.values):
      for i,m in enumerate(mc):
  
          plt.text(n+0.35, i+0.35, str(round(m,2)), color='white', fontsize=24)
  plt.xticks(np.arange(0.5, 5.5, 1))
  plt.yticks(np.arange(0.5, 5.5, 1))
  labels = list(df.columns) # ['Video Access Fraction', 'Video Access Density', 'Course Grade', 'FMCE Pre', 'FMCE post']
  ax.set_xticklabels(labels, rotation=90, fontsize=12)
  ax.set_yticklabels(labels, rotation=0, fontsize=12)
