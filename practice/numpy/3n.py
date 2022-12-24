import numpy as num
print("0 dimension array")
k=num.array(45)#0 dimension array
j=num.array([1,3,4])#one dimension array
l=num.array([[1,2,3],[5,6,7]])#two dimension array
m=num.array([[[1,2,3],[1,2,3]],[[4,5,6],[6,7,8]]])#three dimension array
print(k)
print("1 dimension array")
print(j)
print("2 dimension array")
print(l)
print("3 dimension array")
print(m)

#check the dimension of the array

print(k.ndim)
print(j.ndim)
print(l.ndim)
print(m.ndim)

a=num.array([1,2,3],ndmin=4)
print(a)
print(a.ndim)