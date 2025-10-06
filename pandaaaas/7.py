#Q7

import pandas as pd

S1 = pd.Series([39, 41, 42, 44], index=['A', 'B', 'C', 'D'])
S2 = pd.Series([10, 10, 10, 10], index=['A', 'B', 'D', 'F'])

print(S1[:2] * 100)
print(S1 * S2)
print(S2[::-1] * 10)

# Output:
# A    3900
# B    4100
# dtype: int64

# A    390.0
# B    410.0
# C      NaN
# D    440.0
# F      NaN
# dtype: float64

# F    100
# D    100
# B    100
# A    100
# dtype: int64
