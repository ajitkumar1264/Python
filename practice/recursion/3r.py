def fibonacci(n):
    if(n<=1):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("enter the number : "))
k=0
for x in range(1,50):
    print(fibonacci(x))
    k=k+1
    if(k==n):
        break
    
  