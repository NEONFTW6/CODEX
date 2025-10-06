#Q4

import pandas as pd

Series1 = pd.Series([95, 89, 92, 95], index=['IP', 'Physics', 'Chemistry', 'Math'])

print(Series1['IP'])

Series1 += 10

print(Series1)

# Output:
# 95
# IP          105
# Physics      99
# Chemistry   102
# Math        105
# dtype: int64
