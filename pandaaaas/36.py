#Q36

import pandas as pd

s13 = pd.Series([6700, 8000, 5400, 3400], index=['A', 'B', 'C', 'D'])

s13.index = range(0, 4)  # Correct the index length to match the number of elements
print(s13)

# Output:
# 0    6700
# 1    8000
# 2    5400
# 3    3400
# dtype: int64
