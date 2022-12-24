import numpy as num

k=num.array([10,15,25,5])

j=num.diff(k)
z=num.diff(k,n=2)
print(j)
print(z)