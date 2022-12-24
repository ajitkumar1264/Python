l=[]
def convert(b):
    if(b==0):
        return l
    k=b%10
    l.append(k)
    convert(b//2)

n=int(input("Enter the number : "))
convert(n)
print(l)



