#Q37

import pandas as pd

first = [7, 8, 9]
second = pd.Series(first)
s1 = pd.Series(data=first*2)
s2 = pd.Series(data=second*2)

print("Series1:")
print(s1)
print("Series2:")
print(s2)

# Output:
# Series1:
# 0    7
# 1    8
# 2    9
# 3    7
# 4    8
# 5    9
# dtype: int64

# Series2:
# 0    14
# 1    16
# 2    18
# dtype: int64
