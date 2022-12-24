def uniquelist(l):
    x=[]
    for i in l:
        if i not in x:
            x.append(i)
    return x

print(uniquelist([1,2,3,2,4,4]))
