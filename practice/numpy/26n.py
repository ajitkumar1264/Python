from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
#logistic distribution 
k=random.logistic(loc=1,scale=2,size=(2,3))
sns.distplot(k)
plt.show()
print(k)