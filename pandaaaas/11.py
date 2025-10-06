#Q11

import pandas as pd

a = [10, 20, 25, 50]
b = pd.Series([10, 20, 25, 50])

print(a * 2)
print(b * 2)

# Output:
# [10, 20, 25, 50, 10, 20, 25, 50]

# 0     20
# 1     40
# 2     50
# 3    100
# dtype: int64

