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
ax = sns.boxplot(x='Month', y='Convert ng/g', data = df, color = 'gray')
plt.setp(ax.get_xticklabels(), rotation=0)

# Label the axes
_=plt.xlabel('Month')
_=plt.ylabel('Testosterone Concentration (ng/g)')



# # Calculate number of obs per group & median to position labels
# medians = df.groupby(['Month'])['Convert ng/g'].median().values
# nobs = df['Month'].value_counts().values
# nobs = [str(x) for x in nobs.tolist()]
# nobs = ["n: " + i for i in nobs]
#
# # Add it to the plot
# pos = range(len(nobs))
# for tick, label in zip(pos, ax.get_xticklabels()):
#     ax.text(pos[tick], medians[tick] + .85, nobs[tick],
#             horizontalalignment='center', size='small', color='black', weight='semibold')

#Show the plot
plt.show()

#Describe (Mean and Std)
print(df.groupby("Month")['Convert ng/g'].describe())


#Create 2 subset dataframes to compare
jan =df[(df['Month'] == 'January')]
feb =df[(df['Month'] == 'February')]
mar =df[(df['Month'] == 'March')]
apr =df[(df['Month'] == 'April')]
may =df[(df['Month'] == 'May')]
jul =df[(df['Month'] == 'July')]
aug =df[(df['Month'] == 'August')]
sep =df[(df['Month'] == 'September')]
oct =df[(df['Month'] == 'October')]
nov =df[(df['Month'] == 'Novemeber')]
dec =df[(df['Month'] == 'December')]

#Test normality
# print('Normality Test: W test statistic and P-Value')
# print(stats.shapiro(hawaii['Convert ng/g']))
# print(stats.shapiro(alaska['Convert ng/g']))
#
#
#Conduct one-way Anova
print('ANOVA Results')
print(stats.f_oneway(jan['Convert ng/g'], feb['Convert ng/g'], mar['Convert ng/g'], apr['Convert ng/g'],
                     jun['Convert ng/g'], jul['Convert ng/g'], aug['Convert ng/g'],
                     sep['Convert ng/g'], oct['Convert ng/g'], nov['Convert ng/g'], dec['Convert ng/g']))
print('Kruskal Results')
print(stats.kruskal(jan['Convert ng/g'], feb['Convert ng/g'], mar['Convert ng/g'], apr['Convert ng/g'],
                    jun['Convert ng/g'], jul['Convert ng/g'], aug['Convert ng/g'],
                     sep['Convert ng/g'], oct['Convert ng/g'], nov['Convert ng/g'], dec['Convert ng/g']))

print(pairwise_tukeyhsd(df['Convert ng/g'], df['Month'], alpha = 0.05))