#Q22

import pandas as pd

s1 = pd.Series(range(2, 11, 2), index=[x for x in "abcde"])

print(s1)

# Output:
# a     2
# b     4
# c     6
# d     8
# e    10
# dtype: int64
