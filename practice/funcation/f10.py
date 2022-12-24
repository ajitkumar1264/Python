def even_number(l):
    u=[]
    for x in l:
        if x%2==0:
            u.append(x)
    return u

print(even_number([1,2,3,4,5,6,7,8,9]))