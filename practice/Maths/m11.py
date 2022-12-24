n=int(input("Enter the Number : "))
num=0
for i in range(1,n):
    if(n%i==0):
        num=num+i
if(n==num):
    print("Enter The Number Is perfect!")
else:
    print("You Entered Number is not perfect!")