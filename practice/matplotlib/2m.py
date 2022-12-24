import matplotlib.pyplot as plt
values=[5,8,9,4,1,6,7,2,3,8]
#line chart created
plt.title("ajitkumar")
values1=[5,4,3,7,8,5.2,4,4,5,4]
plt.plot(range(1,11),values,marker=">",ls="-.",lw=1,c="k")
plt.plot(range(1,11),values1)
plt.xlabel("price")
plt.ylabel("money")
plt.legend(['cx','cy'],loc=4)
plt.show()
#to save the diagram
#plt.savefig("saveToPath.png",format='png')