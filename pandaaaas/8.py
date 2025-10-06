#Q8

import pandas as pd

S1 = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
S2 = pd.Series([5, 4, 6, 8], index=['A', 'B', 'C', 'D'])

S3 = S1 * S2

print(S3)

# Output:
# A     50
# B     80
# C    180
# D    320
# dtype: int64
