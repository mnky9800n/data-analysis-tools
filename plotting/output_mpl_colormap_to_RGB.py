# output colormap to txt file
#
# dependencies: matplotlib


from matplotlib import cm
import csv

with open('ylgnbu.txt', 'wb') as f:

    writer = csv.writer(f, delimiter=' ')
    for c in range(0,255):
        
        # in this case I picked YlGnBu but you can pick any 
        # color map you want.
        
        writer.writerow(cm.YlGnBu(c))
        
    f.close()
