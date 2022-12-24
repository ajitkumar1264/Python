def lcm(x,y):
    if x>y:
        z=x
    else:
        z=y
        while(True):
            if z%x==0 and z%y==0:
              lcd=z
              break
            z=z+1
        return lcd

print(lcm(4,6))


