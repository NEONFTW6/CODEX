#Q29

import pandas as pd

s12 = pd.Series([6700, 8000, 5400, 3400], index=['A', 'B', 'C', 'D'])

s12['A'] = 7500

print(s12)

# Output:
# A    7500
# B    8000
# C    5400
# D    3400
# dtype: int64
