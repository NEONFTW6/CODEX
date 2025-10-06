#Q28

import pandas as pd

s1 = pd.Series([2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e'])

s1[1:5:2] = 345.6
s1[2:4] = -14.65

print(s1)

# Output:
# a      2.00
# b    345.60
# c    -14.65
# d    -14.65
# e      6.00
# dtype: float64
