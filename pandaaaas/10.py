#Q10

import pandas as pd

company = pd.Series([350, 200, 800, 150], index=['TCS', 'Reliance', 'L&T', 'Wipro'])

print(company[company > 250])

company.name = "Profit"

print(company)


# Output:
# (i) Companies with profit > 250:
    
#     TCS    350
#     L&T    800
#     dtype: int64

# (ii) Named Series:
    
#      TCS         350
#      Reliance    200
#      L&T         800
#      Wipro       150
#      Name: Profit, dtype: int64
