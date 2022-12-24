import numpy as num
k=num.array([1,2,3,4,5,6,7,8])
p=[]
for x in k:
    if x%2==0:
        p.append(True)
    else:
        p.append(False)
q=k[p]
print(q)
#directly is possible to reach the solution
#just write the formula after the assignment operator
filter_arry=k>4
#--------------------------
o=k[filter_arry]
#----------------------------
print(o)