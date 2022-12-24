def sumarray(k,size):
    if size==0:
        return 0
    else :
        return k[size-1]+sumarray(k,size-1)

n=int(input("Enter the number to create list : "))
k=list(map(int,str(n)))
print(sumarray(k,len(k)))


