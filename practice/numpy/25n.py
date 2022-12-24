from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
#uniform distribution
k=random.uniform(size=(2,3))
sns.distplot(k,hist=False)
print(k)
plt.show()