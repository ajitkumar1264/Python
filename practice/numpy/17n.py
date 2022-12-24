from numpy import random
#this is for the only integer
k=random.randint(100)
#for the float numbers
w=random.rand()*10
print(k)
print(w)
#size define that generate numbers of array unique numbers
q=random.randint(100,size=(3))
print(q)
#size (first for the dimension,and second for the element or we can say that the numbers)
r=random.randint(50,size=(3,4))
print(r)