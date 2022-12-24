item=[]
num=[x for x in input("Enter the Digit here : ").split(",")]

for p in num:
    x=int(p,2)
    if x%5 !=0:
        item.append(p)

print(",".join(item))