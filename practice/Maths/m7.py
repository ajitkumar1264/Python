n=int(input("enter the number of list"))
b=[]
for i in range(1,n+1):
    k=int(input("Enter the number :"))
    b.append(k)
sum1=0
sum2=0
sum3=0
for j in b:
    if (j>0):
        if(j%2==0):
            sum1+=j
        else:
            sum2+=j
    else:
        sum3+=j
print("the sum of nagative numbers is ",sum3)
print("the sum of Positive numbers even is ",sum1)
print("the sum of Positive numbers odd is ",sum2)
