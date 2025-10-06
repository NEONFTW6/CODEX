#Q15

import pandas as pd
import numpy as np

s = pd.Series(np.arange(10, 50, 10))

print(s)
print(s.ndim)
print(s.shape)
print(len(s))

# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# 1
# (4,)
# 4
