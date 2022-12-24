a=[12,6,5,8,9]

for x in range(1,len(a)):

        key=a[x]
        hole=x
        while x>0 and key < a[hole-1]:
            a[hole]=a[hole-1]
            hole=hole-1
        a[hole]=key

print(a)