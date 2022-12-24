def selection(a):
    for x in range(len(a)):
        min=x
        for i in range(x+1,len(a)):
            if a[i]<a[min]:
                min=i
        a[x],a[min]=a[min],a[x]
            
alist=input("Enter the numbers : ")
alist=[int(x) for x in alist]
selection(alist)
print(alist)