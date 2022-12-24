def insertion(a):
    for x in range(1,len(a)):
        temp=a[x]
        j=x-1
        while j>=0 and temp<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp

alist=input("Enter the number : ")
alist=[int(x) for x in alist]
insertion(alist)
print(alist)