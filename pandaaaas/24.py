#Q24

import pandas as pd
import numpy as np

sections = ['A', 'B', 'C', 'D', 'E']
contributions = [8900, 8700, 7800, 6500, np.nan]

s = pd.Series(contributions, index=sections, dtype='float32')

s = s * 2

print(s)

# Output:
# A    17800.0
# B    17400.0
# C    15600.0
# D    13000.0
# E       NaN
# dtype: float32
