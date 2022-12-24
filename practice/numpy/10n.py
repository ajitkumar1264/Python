import numpy as num
k=num.array([1,2,3,4,5,6])
n=num.array([[1,2,3,4],[5,6,7,8]])
for x in n:
    print(x)
for x in num.nditer(n):
    print(x)
for x,ndx in num.ndenumerate(n):
    print(x,ndx)
for ndx,x in num.ndenumerate(n):
    print(ndx,x)
for ndx,x in num.ndenumerate(k):
    print(ndx,x)