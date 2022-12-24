def reverse(s):
    l=[]
    while(s!=0):
        k=s%10
        if(k!=0):
         #l=l*10+k
         l.append(k)
        s=s//10
    o="".join(l)
    print(o)
reverse(14520)

