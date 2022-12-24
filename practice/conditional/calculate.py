s=input("enter the string here : ")
d=l=0

for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    

print("the characters is " , d)
print("the numbers is ", l)