import pandas as pd
import numpy as np
dates=pd.to_datetime("27th of July, 2020")
i=dates+pd.to_timedelta(np.arange(5),unit='D')
d=[50,53,25,70,60]
time_series=pd.Series(data=d,index=i)
print(time_series)