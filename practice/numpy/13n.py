import numpy as num
k=num.array([1,2,3,4,5,6,7,8])
#where is just give the index of the array not do anything with the array
x=num.where(k==2)
y=num.where(k%2==0)
z=num.where(k%2==1)
print(x)
print("Even numbers index")
print(y)
print("Odd numbers index")
print(z)
a=num.searchsorted(k,3)
print("New funcation output")
print(a)
#search from the right side 
b=num.searchsorted(k,3,side="right")
print(b)
#the correct answere as per mylogic is to be 5 but it will give me 3
#i don't know why i get this answere
