import pandas as pd
#encoding latin1 is most important to read csv file using padas
k=pd.read_csv('E:/Python/practice/pandas/data.csv',encoding="latin1")
#print(k.head())
print(k.to_string())
