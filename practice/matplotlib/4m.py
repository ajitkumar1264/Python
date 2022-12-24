import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5.9,6.2,3.2,8.9,9.7]
l=['1st','2nd','3rd','4th','5th']
c=["b","g",'r',"c","m"]
w=[0.5,0.6,0.3,0.8,0.9]
plt.title("sem Wise spi")
plt.bar(x,y,color=c,label=l,width=w)
plt.show()