import math
print("Enter the coefficient value : ")
l=[]
for i in range(0,4):
    k=int(input("Enter the number : "))
    l.append(k)
x=int(input("Enter the Coefficient value : "))
sum=0
j=3
for i in range(0,3):
    while(j>0):
        sum=sum+(l[i]*math.pow(x,j))
        break
    j=j-1
sum=sum+l[3]
print("the value of the sum is :",sum)

