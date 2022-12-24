def gcd(x,y):
    if x%y==0:
        return x
    for k in range(int(y/2),0,-1):
        if x%k==0 and y%k==0:
            return k

print(gcd(4,6 ))