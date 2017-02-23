import timeit

# bro, probably could just use %timeit if
# you are on ipython. :-P

starttime = timeit.default_timer()

"""
your code here
"""

endtime = timeit.default_timer()
print(endtime - starttime)
