#Q16 Write a program to create a Series having 10 random numbers in the range of 10 and 20.

import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(10, 21, size=10))

print(s)

# Output:
# 0    15
# 1    18
# 2    12
# 3    19
# 4    10
# 5    14
# 6    16
# 7    20
# 8    17
# 9    11
# dtype: int64
