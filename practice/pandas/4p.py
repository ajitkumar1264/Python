import pandas as pd

arr1={
    "data":[1,2,3,4],
    "frame":[5,6,7,8]
}

m=pd.DataFrame(arr1)
print(m.loc[2])