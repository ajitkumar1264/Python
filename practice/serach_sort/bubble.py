def bubble_sort(a):
    for i in range(0,len(a)-1):
        swap=True
        for x in range(i+1,len(a)):
            if a[i]>a[x]:
                a[i],a[x]=a[x],a[i]
                swap=False
        if swap:
            return
""" for x in range(len(a)-1,0,-1):
        no_swap=True
        for j in range(0,x):
            if a[j+1]<a[j]:
                a[j],a[j+1]=a[j+1],a[j]
                no_swap=False
        if no_swap:
            return"""
alist=input("Enter the numbers : ")
alist=[int(x) for x in alist]
bubble_sort(alist)
print(alist)
