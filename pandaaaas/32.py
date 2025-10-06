#Q32

import pandas as pd

s12 = pd.Series([6700, 8000, 5400, 3400], index=['A', 'B', 'C', 'D'])

print(s12[s12 > 5600])

# Output:
# A    6700
# B    8000
# dtype: int64
