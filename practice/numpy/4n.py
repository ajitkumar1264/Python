import numpy as num
k=num.array(45)#0 dimension array
j=num.array([1,3,4])#one dimension array
l=num.array([[1,2,3],[5,6,7]])#two dimension array
m=num.array([[[1,2,3],[1,2,3]],[[4,5,6],[6,7,8]]])#three dimension array
u=num.array([1,2,3],ndmin=5)
print(k)
print(j[1])
print(l[0,1])
print(m[1,1,1])
print(l[0,-1])
print(l.shape)
#the answer is (2,3) which means that 2 dimension where one diminsion of 2 and another was is 3
print(u.shape)