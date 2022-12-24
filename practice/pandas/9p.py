import pandas as pd
i=["name","address","phone","email","website"]
d=["darshan","rj","123","vaghelaajit464@gmail.com","darshan.ac.in"]
s=pd.Series(data=d,index=i)
print(s)