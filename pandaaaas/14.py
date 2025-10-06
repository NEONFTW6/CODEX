#Q14

import pandas as pd

data = [6, 1, 3, 5, 4, 8, 7, 4, 6, 7]
index = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
s1 = pd.Series(data, index=index)

print(s1[3:6])

# Output:
# 7     5
# 9     4
# 11    8
# dtype: int64
