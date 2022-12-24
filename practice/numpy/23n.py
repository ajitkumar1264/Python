import matplotlib.pyplot as plt 
import seaborn as sns
from numpy import random

sns.distplot(random.normal(size=30))

plt.show()