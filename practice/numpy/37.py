import numpy as num

k=num.array([1,1,2,3,5,2,3,4,5,6,7])
arr1=num.array([1,2,3])
arr2=num.array([4,5,3])
jo=num.union1d(arr1,arr2)
bn=num.intersect1d(arr1,arr2)
by=num.setdiff1d(arr1,arr2)
j=num.unique(k)
print(j)
print(bn)
print(by)
print(jo)

