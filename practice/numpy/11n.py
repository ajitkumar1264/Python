import numpy as num

arr1=num.array([[1,2,3],[7,8,9]])
arr2=num.array([[4,5,6],[4,3,2]])
arr3=num.array([1,2,3])
arr4=num.array([3,4,5])

k=num.concatenate((arr1,arr2),axis=1)
#helper funcation with horizontal line
p=num.hstack((arr1,arr2))
#helper funcation with vertical line
q=num.vstack((arr1,arr2))
#for depth stack 
w=num.dstack((arr1,arr2))
print("Horizontal line")
print(p)
print("verticle line print")
print(q)
print("depth line join")
print(w)
print("after the join two array")
print(k)
