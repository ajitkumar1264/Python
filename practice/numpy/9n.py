import numpy as num
k=num.array([1,2,3,4,5,6,7,8,9,10,11,12])
l=num.array([1,2,3,4,5,6,7,8])
o=num.array([[1,2,3],[3,4,5]])
print(k)
newk=k.reshape(3,4)
new_k=k.reshape(2,3,2)
print(newk)
print("3 dimension array")
print(new_k)
print(l.reshape(2,2,-1))
print(o.reshape(-1))