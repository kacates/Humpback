import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)


#Load the data
df = pd.read_csv('a vs c.csv')

#BoxPlot
ax = sns.boxplot(x='Grounds', y='Convert ng/g', data = df, color = 'gray')

# Label the axes
_=plt.xlabel('Location and Age Class')
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
print(df.groupby("Grounds")['Convert ng/g'].describe())


#Create 2 subset dataframes to compare
aa =df[(df['Grounds'] == 'AK-A')]
ac =df[(df['Grounds'] == 'AK-C')]
ha =df[(df['Grounds'] == 'HI-A')]
hc =df[(df['Grounds'] == 'HI-C')]

#Test normality
# print('Normality Test: W test statistic and P-Value')
# print(stats.shapiro(hawaii['Convert ng/g']))
# print(stats.shapiro(alaska['Convert ng/g']))
#
#
#Conduct one-way Anova
print('ANOVA Results')
print(stats.f_oneway(aa['Convert ng/g'], ac['Convert ng/g'], ha['Convert ng/g'], hc['Convert ng/g']))
print('Kruskal Results')
print(stats.kruskal(aa['Convert ng/g'], ac['Convert ng/g'], ha['Convert ng/g'], hc['Convert ng/g']))

print(pairwise_tukeyhsd(df['Convert ng/g'], df['Grounds'], alpha = 0.05))

print(stats.ttest_ind(aa['Convert ng/g'], ac['Convert ng/g'], equal_var = False))
print(stats.ttest_ind(ha['Convert ng/g'], hc['Convert ng/g'], equal_var = False))