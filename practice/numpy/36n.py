import numpy as num
n=3
m=4
u=num.array([1,2,3,4,5,6])
k=num.gcd(n,m)
p=num.gcd.reduce(u)
print(p)
print(k)