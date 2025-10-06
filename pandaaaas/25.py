#Q25

import pandas as pd
import numpy as np

val1 = np.arange(5.25, 50, 10.25)
ser1 = pd.Series(val1, index=['a', 'b', 'a', 'a', 'b'])

print(ser1)
print(ser1['a'])
print(ser1['b'])

# Output:
# a     5.25
# b    15.50
# a    25.75
# a    36.00
# b    46.25
# dtype: float64

# a     5.25
# a     25.75
# a     36.00
# dtype: float64

# b    15.50
# b    46.25
# dtype: float64
