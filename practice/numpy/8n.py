import numpy as num
k=num.array([1,2,3,4,5,6])
x=k.copy()
y=k.view()
y[1]=10
x[1]=12
print("the our copy array")
print(x)
print("the original array")
print(k)
print("the our new view array")
print(y)
print("the our original array")
print(k)
