def relate(n):
    return((abs(1000-n)<=100) or (abs(2000-n)<=100))

print(relate(1950))
print(relate(950))
print(relate(450))