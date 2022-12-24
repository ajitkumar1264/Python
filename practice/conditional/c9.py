lines=[]
while True:
    l=input("enter the lines : ")
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print("".join(l))