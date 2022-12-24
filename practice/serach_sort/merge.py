def merge_sort(a,start,end):
    if end-start>1:
        mid=(start+end)//2
        merge_sort(a,start,mid)
        merge_sort(a,mid,end)
        merge_list(a,start,mid,end)

def merge_list(a,start,mid,end):
    left=a[start:mid]

    right=a[mid:end]
    
    k=start
    i=0
    j=0
    while (start+i<mid and mid+j<end):
        if (left[i]<=right[j]):
            a[k]=left[i]
            i=i+1
        else:
            a[k]=right[j]
            j=j+1
        k=k+1
    if start+i<mid:
        while k<end:
           a[k]=left[i]
           i=i+1
           k=k+1
    else:
        while k<end:
            a[k]=right[j]
            j=j+1
            k=k+1
alist=input("Enter the numbers : ")
alist=[int(x) for x in alist]
merge_sort(alist,0,len(alist))
print(alist)

