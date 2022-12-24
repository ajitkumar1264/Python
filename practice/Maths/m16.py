a=int(input("Enter the numbers you want prime : "))
l=[]
k=0
for x in range(2,50):
    flag=0
    for i in range(2,x):
        if(x%i==0):
            flag=1
    if(flag==0):
        l.append(x)
        k=k+1
    if(k==a):
        break
    
    
print(l)
    



  