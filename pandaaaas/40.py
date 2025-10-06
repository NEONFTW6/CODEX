#Q40

import pandas as pd

D = {'a': 10, 'b': 11, 'c': 12}
S = pd.Series(D, index=['b', 'c', 'd', 'a'])

print(S)

# Output:
# b    11.0
# c    12.0
# d     NaN
# a    10.0
# dtype: float64
