def binary_search(a,key):
    low=0
    high=len(a)
    while low<high:
        mid=(low+high)//2
        if a[mid]==key:
            return mid
        elif a[mid]>key:
            high=mid
        elif a[mid]<key:
            low=mid+1
    return -1
        
alist=input("Enter the number : ")
alist=[int(x) for x in alist]
key=int(input("Enter the value of the key : "))
l=binary_search(alist,key)
if l==-1:
    print("{} is not found".format(key))
else :
    print("{} is found in the place of the {}".format(key,l))