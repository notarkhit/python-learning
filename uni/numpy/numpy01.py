import numpy as np
import math


# nArray = np.arange(1,10)
# nArray = np.full((3,4),8)

nArray = np.array([1,2,3,4])
mArray = np.array([1,2,4,6])

print(any(mArray > nArray))
print(all(mArray > nArray))
print (mArray > nArray)
