l=[]
def sum(n):
    if(n==0):
      return 1
    dig=n%10
    l.append(dig)
    sum(n//10)
a=int(input("Enter the number : "))
sum(a)
print(sum((l)))
