import numpy as np 
"""x=np.zeros([3,2],dtype=int)
print(x)"""
"""x=np.ones([3,2],dtype=int)
print(x)"""
"""x=np.linspace(0,1,10)
print(x)"""
"""x=np.logspace(1.0,2.0,num=10)
print(x)"""
dt=np.dtype([('name',"S10"),('age',int)])
arr2=np.array([("darshan",200),("Abc",300),("xyz",100)],dtype=dt)
arr2.sort(order="name")
print(arr2)