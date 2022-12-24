n=int(input("enter the number :"))
temp=n
k=0
while(n>0):
    k=k+1
    n=n//10
b=str(temp)
c=str(k)
print(int(c+b[k-1]))