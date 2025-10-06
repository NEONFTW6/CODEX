#Q17

import pandas as pd
import numpy as np

s = pd.Series([4.0, 5.0, 7.0, np.nan, 1.0, 10.0])

s1 = s + 1
print(s1)

s2 = s.fillna(0)
print(s2)

# Output:
# 0     5.0
# 1     6.0
# 2     8.0
# 3     NaN
# 4     2.0
# 5    11.0
# dtype: float64

# 0     4.0
# 1     5.0
# 2     7.0
# 3     0.0
# 4     1.0
# 5    10.0
# dtype: float64
