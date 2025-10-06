#Q1

import pandas as pd

Series1 = pd.Series([100, 200, 300, 400, 500], index=['A', 'B', 'C', 'D', 'E'])
Series2 = Series1 * 2
print(Series2)


# Output:
# A     200
# B     400
# C     600
# D     800
# E    1000
# dtype: int64
