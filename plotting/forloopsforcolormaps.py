import matplotlib
import matplotlib.pyplot as plt
import numpy as np

cmap = matplotlib.cm.get_cmap('Spectral')
# rgba = cmap()

fig, ax1 = plt.subplots(1)

for n in range(10):
    x = np.random.random(7)
    y = x+1
    a = x[4]
    ax1.plot(x, a*y, color=cmap(float(n)/10), zorder=5)

ax2 = fig.add_axes([0.2, 1.0, 0.6, 0.05])
    
norm = matplotlib.colors.Normalize(vmin=0, vmax=10,)
matplotlib.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, orientation='horizontal')
