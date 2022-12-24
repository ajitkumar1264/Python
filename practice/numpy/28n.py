import numpy as num
print(type(num.add))
print(type(num.concatenate))
j=type(num.add)
if j==num.ufunc:
    print("add funcation is ufunc")
else:
    print("add funcation is not ufunc")