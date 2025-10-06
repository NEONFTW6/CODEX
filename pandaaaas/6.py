#Q.6-	What will be the output produced by the following programming statements1&2?

import pandas as pd 
S1=pd.Series(data=[31,41,51]) 
print(S1>40)	
print(S1[S1>40])	

# Output:
# 1    41
# 2    51
# dtype: int64
