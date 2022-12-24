x=input("if you want to enter a number write y or no to write n : ")
h=[]
even=0
odd=0
while x.upper()=="Y":
      a=int(input("enter the number : "))
      h.append(a)
      x=input("if you want to enter a number write y or no to write n : ")
      if x.upper()=="N":
        break

if len(h)==0:
    print("No number is present in the list")
    quit()

for x in h:
    if x%2==0:
        even+=1
    else:
        odd+=1

print("Total odd number ",odd,"Even number",even)
     