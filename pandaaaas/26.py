#Q26

import pandas as pd

students = pd.Series([39, 31, 32, 34, 35], index=['A', 'B', 'C', 'D', 'E'])

ticket_price = 100
collected_A_B = students[['A', 'B']] * ticket_price

print(collected_A_B)

# Output:
# A    3900
# B    3100
# dtype: int64
