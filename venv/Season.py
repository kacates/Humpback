import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)


#Load the data
df = pd.read_csv('adultblubber.csv')

#BoxPlot
ax = sns.boxplot(x='Season', y='Convert ng/g', data = df, color = 'gray')

# Label the axes
_=plt.xlabel('Season')
_=plt.ylabel('Testosterone Concentration (ng/g)')

# # Calculate number of obs per group & median to position labels
# medians = df.groupby(['Season'])['Convert ng/g'].median().values
# nobs = df['Season'].value_counts().values
# nobs = [str(x) for x in nobs.tolist()]
# nobs = ["n: " + i for i in nobs]
#
# # Add it to the plot
# pos = range(len(nobs))
# for tick, label in zip(pos, ax.get_xticklabels()):
#     ax.text(pos[tick], medians[tick] + 2, nobs[tick],
#             horizontalalignment='center', size='small', color='black', weight='semibold')

#Show the plot
plt.show()

#Describe (Mean and Std)
print(df.groupby("Season")['Convert ng/g'].describe())


#Create 2 subset dataframes to compare
summer =df[(df['Season'] == 'SUMMER')]
spring =df[(df['Season'] == 'SPRING')]
winter =df[(df['Season'] == 'WINTER')]
fall =df[(df['Season'] == 'FALL')]

#Test normality
# print('Normality Test: W test statistic and P-Value')
# print(stats.shapiro(hawaii['Convert ng/g']))
# print(stats.shapiro(alaska['Convert ng/g']))
#
#
#Conduct one-way Anova
print('ANOVA Results')
print(stats.f_oneway(summer['Convert ng/g'], spring['Convert ng/g'], winter['Convert ng/g'], fall['Convert ng/g']))
print('Kruskal Results')
print(stats.kruskal(summer['Convert ng/g'], spring['Convert ng/g'], winter['Convert ng/g'], fall['Convert ng/g']))

print(pairwise_tukeyhsd(df['Convert ng/g'], df['Season'], alpha = 0.05))