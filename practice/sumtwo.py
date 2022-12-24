def twosum(x,y,z):
    
    if x ==y or y==z or x==z:
        sum=0
        return sum
    else:
        sum=x+y+z
        return sum

print(twosum(4,5,5))
    