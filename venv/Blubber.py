import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)


#Load the data
df = pd.read_csv('blubber.csv')

#BoxPlot
ax = sns.boxplot(x='Sample Type', y='Convert ng/g', data = df, color = 'gray')

# Label the axes
_=plt.xlabel('Sample Location and Tissue Type')
_=plt.ylabel('Testosterone Concentration (ng/g)')

# # Calculate number of obs per group & median to position labels
# medians = df.groupby(['Sample Type'])['Convert ng/g'].median().values
# nobs = df['Sample Type'].value_counts().values
# nobs = [str(x) for x in nobs.tolist()]
# nobs = ["n: " + i for i in nobs]
#
# # Add it to the plot
# pos = range(len(nobs))
# for tick, label in zip(pos, ax.get_xticklabels()):
#     ax.text(pos[tick], medians[tick] + .75, nobs[tick],
#             horizontalalignment='center', size='small', color='black', weight='semibold')

#Show the plot
plt.show()

#Describe (Mean and Std)
print(df.groupby("Sample Type")['Convert ng/g'].describe())


#Create 2 subset dataframes to compare
akb =df[(df['Sample Type'] == 'AK-B')]
aks =df[(df['Sample Type'] == 'AK-S')]
hb =df[(df['Sample Type'] == 'HI-B')]
hs =df[(df['Sample Type'] == 'HI-S')]

#Test normality
# print('Normality Test: W test statistic and P-Value')
# print(stats.shapiro(hawaii['Convert ng/g']))
# print(stats.shapiro(alaska['Convert ng/g']))
#
#
#Conduct one-way Anova
print('ANOVA Results')
print(stats.f_oneway(akb['Convert ng/g'], aks['Convert ng/g'], hb['Convert ng/g'], hs['Convert ng/g']))
print('Kruskal Results')
print(stats.kruskal(akb['Convert ng/g'], aks['Convert ng/g'], hb['Convert ng/g'], hs['Convert ng/g']))

print(pairwise_tukeyhsd(df['Convert ng/g'], df['Sample Type'], alpha = 0.05))