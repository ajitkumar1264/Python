row=4
stop=2
currentnumber=1

for i in range(row):
    for x in range(1,stop):
        print(currentnumber,end="")
        currentnumber+=1
    print("\r")
    stop+=1