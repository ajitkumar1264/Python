import pandas as pd

a=[7,5,4]
u={
    "one":100,
    "two":200,
    "three":300
}
h=pd.Series(a,index=["x","y","z"])
print(h)
print(h["x"])
c=pd.Series(u,index=["one","two"])
print(c)