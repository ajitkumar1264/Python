a=int(input("Enter the number : "))
b=int(input("Enter the second number :"))
if(a>b):
    min=b
else:
    min=a
while(1):
    if(min%a==0 and min%b==0):
        print("the lcm is ",min)
        break
    min=min+1