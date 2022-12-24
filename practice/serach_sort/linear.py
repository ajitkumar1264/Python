def linear_search(a,key):
    for x in range(len(a)):
        if a[x]==key:
            return x
    return -1
    

alist=input("enter the list of the numbers : ")
#alist=alist.split()
alist=[int(x) for x in alist]
key=int(input("Enter the value of the key : "))
j=linear_search(alist,key)
if(j==-1):
    print("{} is not found in the list".format(key))
else:
    print("{} is found in the place of the {}".format(key,j))