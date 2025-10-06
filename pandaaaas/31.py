#Q31

import pandas as pd

s3 = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5], index=['a', 'b', 'c', 'd', 'e'])

print(s3 + 3)
print(s3 * 2)
print(s3[s3 > 3.0])

# Output:
# a     4.5
# b     6.0
# c     7.5
# d     9.0
# e    10.5
# dtype: float64

# a     3.0
# b     6.0
# c     9.0
# d    12.0
# e    15.0
# dtype: float64

# c    4.5
# d    6.0
# e    7.5
# dtype: float64
