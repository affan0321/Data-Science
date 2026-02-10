import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
print(x)
y = x**2
print(y)

print(plt.plot(x,y))

fig = plt.figure()
axis1 = fig.axes([0.1,0.1,0.8,0.8])
axis1.plot(x,y)


import matplotlib as plt
import seaborn as sns

df = sns.load_dataset("tips")
df

sns.countplot(x = df["sex"], hue = df["smoker"] )
sns.barplot(x = df['sex'], y = df['total_bill'])

import numpy as np

sns.barplot(x = df['sex'], y = df['total_bill'], estimator = np.sum)
sns.boxplot(x = 'tip', y = 'day',data = df, palette = 'rainbow')
sns.violinplot(x = 'day', y = 'total_bill',data = df)
sns.stripplot(x ='day', y = 'total_bill', data= df)
sns.violinplot(x = 'tip', y = 'day',data = df)
sns.swarmplot(x = 'tip', y = 'day',data = df)

flights = sns.load_dataset('flights')
flights

tips = sns.load_dataset('tips')
tips

tipscorr = tips[['total_bill','tip','size']]
tipscorr

tipscorr.corr()

sns.heatmap(tipscorr.corr(),annot = True)
sns.clustermap(tipscorr.corr(),annot = True)
pvtflights = flights.pivot_table(values = 'passengers',index = 'month',columns = 'year')
pvtflights