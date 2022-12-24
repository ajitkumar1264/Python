row=5
nums=row+1
for x in range(row,0,-1):
    nums=nums-1
    for i in range(x):
        print(nums,end="")
        
    print(" ")