def GCD(x,y):
    if x>y:
        max=x
    else:
        max=y
    for i in range(1,max+1):
        if(x%i==0 and y%i==0):
            gcd=i
    return gcd

x=int(input("Enter the first number : "))
y=int(input("Enter the second number : "))  
print(GCD(15,5))
