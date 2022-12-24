def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(a,a%b)
v=int(input("enter thr first number :  "))
l=int(input("enter the second number : "))
print(GCD(v,l))