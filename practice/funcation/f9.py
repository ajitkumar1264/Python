def prime(a):
    if a==1:
        return False
    elif a==2:
        return True
    else:   
        for x in range(2,a):
           if (a%x==0):
            return False
        return True

print(prime(9))
