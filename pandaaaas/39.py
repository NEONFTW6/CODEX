#Q39

import pandas as pd
import numpy as np

data = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
s = pd.Series(data, index=[101, 102, 103, 104, 105, 106, 107])

print(s[[103, 105, 107]])

# Output:
# 103     Wed
# 105     Fri
# 107     Sun
# dtype: object
