import numpy as num

k=num.array([1,2,3,4])
y=num.array([5,6,7,8])

j=num.prod(k)
w=num.prod([k,y],axis=1)
t=num.cumprod(k)
print(t)
print(j)
print(w)