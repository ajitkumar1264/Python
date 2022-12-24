a=[12,5,6,8,9]


for x in range(len(a)-1):
    key=x
    for y in range(x+1,len(a)):
        if a[key]>a[y]:
            key=y      
    temp=a[key]
    a[key]=a[x]
    a[x]=temp

for x in a:
    print(x)
    