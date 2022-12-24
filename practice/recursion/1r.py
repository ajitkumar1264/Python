def check(n):
    if(n<2):
        return (n%2==0)
    return check(n-2)
k=int(input("Enter the number : "))
if(check(k)==True):
    print("The number is even number ")
else :
    print("the number is odd number")