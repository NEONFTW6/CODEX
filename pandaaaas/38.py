#Q38

import pandas as pd
import numpy as np

data = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
s = pd.Series(data)

print(s[:4])
print(s[-4:])

# Output:
# 0    Mon
# 1    Tue
# 2    Wed
# 3    Thu
# dtype: object

# 3     Thu
# 4     Fri
# 5     Sat
# 6     Sun
# dtype: object
