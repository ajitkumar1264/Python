def quicksort(a,start,end):
    if end-start>1:
        p=partion(a,start,end)
        quicksort(a,start,p)
        quicksort(a,p+1,end)
def partion(a,start,end):
    paivot=a[start]
    i=start+1
    j=end-1
    while True:
        while i<=j and a[i]<=paivot:
            i=i+1
        while i<=j and a[j]>=paivot:
            j=j-1
        if i<=j:
            a[i],a[j]=a[i],a[j]
        else:
            a[start],a[j]=a[j],a[start]
            return j
alist=input("enter the numbers : ")
alist=[int(x) for x in alist]
quicksort(alist,0,len(alist))
print(alist)
