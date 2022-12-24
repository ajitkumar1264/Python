import numpy as num
x=[1,2,3,4]
y=[5,6,7,8]
b=num.array([-1,-2,-3])
u=num.array([10,20,30])
o=num.array([1,2,5])

j=num.add(x,y)
m=num.subtract(y,x)
n=num.multiply(x,y)
k=num.divide(y,x)
d=num.absolute(b)
p=num.remainder(u,o)
s=num.power(u,o)
print(s)
print(p)
print(d)
print("the sum={} and subtract={} and multiply={} and divide={}".format(j,m,n,k))