from numpy import random

k=random.choice([2,3,4,5])
print(k)
j=random.choice([2,3,5,6],size=(2,3))
print(j)
x=random.choice([2,3,4],p=[0.2,0.5,0.3],size=(40))
print("example of the data distribution")
print(x)
sum1=0
sum2=0
sum3=0
for i in x:
    if i==2:
        sum1=sum1+1
    elif i==3:
        sum2=sum2+1
    else:
        sum3=sum3+1
print("the sum1= {} and sum2= {} and sum3={}".format(sum1,sum2,sum3))
w=random.choice([1,2,3],p=[0.2,0.3,0.5],size=(2,3))
print(w)