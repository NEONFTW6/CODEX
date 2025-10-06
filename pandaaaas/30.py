#Q30 A Series object training data consists of 2000 rows of data.
#Write a program to print(i) First 100 rows of data (ii) Last 5 rows of data

import pandas as pd

trainingdata = pd.Series(range(1, 2001))

print(trainingdata.head(100))
print(trainingdata.tail(5))

# Output:
# 0      1
# 1      2
# 2      3
# 3      4
# 4      5
#        ..
# 95    96
# 96    97
# 97    98
# 98    99
# 99   100
# dtype: int64

# 1995    1996
# 1996    1997
# 1997    1998
# 1998    1999
# 1999    2000
# dtype: int64

