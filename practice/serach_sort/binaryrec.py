def binary_search_re(a,low,high,key):
    if not low<high:
        return -1
    mid=(low+high)//2
    if a[mid]==key:
        return mid
    elif a[mid]>key:
        return binary_search_re(a,low,mid,key)
    elif a[mid]<key:
        return binary_search_re(a,mid+1,high,key)


alist=input("enter the numbers : ")
alist=[int(x) for x in alist]
key=int(input("Enter the key value here  : "))
j=binary_search_re(alist,0,len(alist),key)
if j==-1:
    print("{} is not found in this list".format(key))
else:
    print("{} is found in the place of the {}".format(key,j))
