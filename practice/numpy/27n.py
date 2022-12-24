import numpy as num
x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=[]
#here we used zip method two sum of the two array element
for i,j in zip(x,y):
    z.append(i+j)
print(z)
#but to do easy in this we can use numpy funcation add
o=num.add(x,y)
print(o)