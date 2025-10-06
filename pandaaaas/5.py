#Q5

import pandas as pd

SQTR = pd.Series([50000, 65890, 56780, 89000, 77900], index=['QTR1', 'QTR2', 'QTR3', 'QTR4', 'QTR5'])

print(SQTR)

# Output:
# QTR1    50000
# QTR2    65890
# QTR3    56780
# QTR4    89000
# QTR5    77900
# dtype: int64
