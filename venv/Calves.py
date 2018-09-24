import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#Load the data
df = pd.read_csv('calves.csv')

#BoxPlot
ax = sns.boxplot(x='Grounds', y='Convert ng/g', data = df, color = 'gray')

# Label the axes
_=plt.xlabel('Biopsy Location')
_=plt.ylabel('Testosterone Concentration (ng/g)')

# Calculate number of obs per group & median to position labels
# medians = df.groupby(['Grounds'])['Convert ng/g'].median().values
# nobs = df['Grounds'].value_counts().values
# nobs = [str(x) for x in nobs.tolist()]
# nobs = ["n: " + i for i in nobs]
#
# # Add it to the plot
# pos = range(len(nobs))
# for tick, label in zip(pos, ax.get_xticklabels()):
#     ax.text(pos[tick], medians[tick] + .5, nobs[tick],
#             horizontalalignment='center', size='small', color='black', weight='semibold')

#Show the plot
plt.show()

#Describe (Mean and Std)
print(df.groupby("Grounds")['Convert ng/g'].describe())


#Create 2 subset dataframes to compare
hawaii =df[(df['Grounds'] == 'HI')]
alaska =df[(df['Grounds'] == 'AK')]

#Test normality
# print('Normality Test: W test statistic and P-Value')
# print(stats.shapiro(hawaii['Convert ng/g']))
# print(stats.shapiro(alaska['Convert ng/g']))
#
#
#Conduct welch's t-test
print('Welchs T-Test')
print(stats.ttest_ind(hawaii['Convert ng/g'], alaska['Convert ng/g'], equal_var = False))
