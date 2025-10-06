#Q34

import pandas as pd

S1 = pd.Series([10, 20, 30, 40, 50])
S2 = pd.Series([0, 1, 2, 3, 4])
S3 = pd.Series([5, 10, 15, 20, 25])

print(S1 + S2)
print(S1 * S3)
print(S1 - S2)

# Output:
# 0     10
# 1     21
# 2     32
# 3     43
# 4     54
# dtype: int64

# 0     50
# 1    200
# 2    450
# 3    800
# 4   1250
# dtype: int64

# 0     10
# 1     19
# 2     28
# 3     37
# 4     46
# dtype: int64
