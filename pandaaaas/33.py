#Q33 

import pandas as pd

c11 = pd.Series([150, 200, 180], index=['Science', 'Commerce', 'Humanities'])
c12 = pd.Series([160, 210, 190], index=['Science', 'Commerce', 'Humanities'])

total_students = c11 + c12

print(total_students)

# Output:

# Science      310
# Commerce     410
# Humanities   370
# dtype: int64


