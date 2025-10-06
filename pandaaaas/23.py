#Q23

import pandas as pd
import numpy as np

x = np.arange(10, 15)
s3 = pd.Series(index=x, data=x * 2)
s4 = pd.Series(x ** 2, x)

print(s3)
print(s4)

# Output:
# 10    20
# 11    22
# 12    24
# 13    26
# 14    28
# dtype: int64

# 10    100
# 11    121
# 12    144
# 13    169
# 14    196
# dtype: int64

