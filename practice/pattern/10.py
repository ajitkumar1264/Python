rows=5

for i in range(rows):
    for j in range(1,i):
        print(j,end="")
    for k in range(i,0,-1):
        print(k,end="")
    
    print("")