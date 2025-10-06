#Q35

import pandas as pd

s12 = pd.Series([6700, 8000, 5400, 3400], index=['D', 'A', 'B', 'C'])

print(s12.sort_values(ascending=False))
print(s12.sort_index(ascending=True))

# Output:

# A    8000
# D    6700
# B    5400
# C    3400
# dtype: int64

# A    8000
# B    5400
# C    3400
# D    6700
# dtype: int64
