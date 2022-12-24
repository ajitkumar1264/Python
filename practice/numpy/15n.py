import numpy as num
k=num.array([1,2,3,4])
x=[True,False,True,False]
newarr=k[x]
print(newarr)
j=num.array([40,41,42,43,44,45,46,47])
p=[]
for i in j:
    if i>42:
        p.append(True)
    else:
        p.append(False)

newarr1=j[p]
print("old array is ",j)
print("The Filter array is ",newarr1)