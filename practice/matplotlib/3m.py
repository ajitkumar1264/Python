import matplotlib.pyplot as plt
values=[305,201,805,35,436]
l=["food",'travel',"Accomdation","mics","shoping"]
c=['b','g','r','c','m']
e=[0,0.1,0,0,0]
#pie chart
plt.pie(values,colors=c,labels=l,explode=e)
plt.show()