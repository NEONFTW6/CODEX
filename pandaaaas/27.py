#Q27

import pandas as pd

S4 = pd.Series([2.50, 17.45, 20.25, 87.25, 33.76])

S4[0] = 1.75
S4[2:4] = -23.74

print(S4)

# Output:
# 0     1.75
# 1    17.45
# 2   -23.74
# 3   -23.74
# 4    33.76
# dtype: float64
