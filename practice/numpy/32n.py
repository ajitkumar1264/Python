import numpy as num

k=num.array([1,2,3])
u=num.array([4,5,6])

h=num.add(k,u)
j=num.sum([k,u])
t=num.sum([k,u],axis=1)
b=num.cumsum(k)
print(b)
print(h)
print(j)
print(t)