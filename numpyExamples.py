#Let's do some experiments to understand why to use numpy and what we can do with it.

#import numpy with alias np
import numpy as np

import sys

# one dimensional array
a=np.array([1,2,3])
print(a)

# two dimensional array
a= np.array([(1,2,3),(4,5,6)])
print(a)

#why numpy better than list..
#1)Less memory
#2)faste2
#3)Convenien3

r = range(1000)

print(sys.getsizeof(0)*len(r))


d = np.arange(1000)
print(d.size *d.itemsize)
#so python int value is taking 28*1000 as total size, where as numpy is taking 4*1000.
