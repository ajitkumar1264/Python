import numpy as num
k=num.array(45)#0 dimension array
j=num.array([1,3,4,5,6,7,8,9])#one dimension array
l=num.array([[1,2,3],[5,6,7]])#two dimension array
m=num.array([[[1,2,3],[1,2,3]],[[4,5,6],[6,7,8]]])#three dimension array
print(j[2:5])
print(j[2:])
print(k.dtype)
h=num.array(["ajit","hardik","vishn45"])
print(h.dtype)