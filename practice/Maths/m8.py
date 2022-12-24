n=int(input("Enter the number in list :"))
b=[]
for x in range(1,n+1):
    k=int(input("Enter the number :"))
    b.append(k)
c1=[]
c2=[]
for x in b:
    if (x%2==0):
        c1.append(x)
    else:
        c2.append(x)
c1.sort()
c2.sort()
count1=0
count2=0
for x in c1:
    count1+=1
for y in c2:
    count2+=1
print("The largest greater even number is ",c1[count1-1])
print("The largest greater odd number is ",c2[count2-1])