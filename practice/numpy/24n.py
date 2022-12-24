from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
#poisson distribution
x=random.poisson(lam=2,size=10)
#print(x)
sns.distplot(random.binomial(n=1000,p=0.01,size=1000),label="binomial")
sns.distplot(random.poisson(lam=10,size=1000),label="poisson")

plt.show()

