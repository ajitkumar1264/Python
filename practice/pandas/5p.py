import pandas as pd

data={
    "calories":[420,380,524],
    "duration":[20,30,40]
}

df=pd.DataFrame(data,index=["one","two","three"])
print(df)
print(df.loc["two"])