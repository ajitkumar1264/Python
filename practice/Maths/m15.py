x=int(input("enter the first number : "))
y=int(input("enter the second number : "))
sum1=0
sum2=0
for i in range(1,x):
    if(x%i==0):
        sum1+=i
for i in range(1,y):
    if(y%i==0):
        sum2+=i
if(sum1==y and sum2==x):
    print("Amicable!")
else:
    print("Not Amicable!")