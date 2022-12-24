temp=input("Input the Tempretuare you like to convert ?")
degree=int(temp[:-1])
i_convention=temp[-1]

if i_convention.upper() =="C":
    result=int(round((9*degree)/5+32))
elif i_convention.upper()=="F":
    result=int(round((5/9)*(degree-32)))
else:
    print("Input the any valid NumberConvention")
    

print("the ans of ",i_convention,"is",result)