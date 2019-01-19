import bisect
impot copy
import random

# a random integer N: a <= N <= b
N = random.randint(a, b) 

# binary search
# find index to insert x into a 
i = bisect.bisect(a, x, low=0, high=len(a))      # after x if x exists
i = bisect.bisect_left(a, x, low=0, high=len(a)) # before x if x exists

# deep copy
l = [1]
l2 = copy.deepcopy(l)
