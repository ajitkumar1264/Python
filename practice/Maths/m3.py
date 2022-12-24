n=int(input("enter the interger"))
print("Factors are :")
i=1
#factors find trick
while(i<=n):
    if (n%i==0):
        print(i)
    i+=1
#prime numbers find trick
k=2
while(k<n):
    if(n%k==0):
       flag=1
    k+=1
if flag==1:
    print("this is not a prime number")
else:
    print("This the prime number is ",n)


