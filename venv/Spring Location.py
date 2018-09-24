import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#Load the data
df = pd.read_csv('adultblubber.csv')

#BoxPlot
ax = sns.boxplot(x='Spring_Location', y='Concentration', data = df, color = 'gray')

# Label the axes
_=plt.xlabel('Spring Location')
_=plt.ylabel('Testosterone Concentration (ng/g)')

# # Calculate number of obs per group & median to position labels
# medians = df.groupby(['Spring_Location'])['Concentration'].median().values
# nobs = df['Spring_Location'].value_counts().values
# nobs = [str(x) for x in nobs.tolist()]
# nobs = ["n: " + i for i in nobs]
#
# # Add it to the plot
# pos = range(len(nobs))
# for tick, label in zip(pos, ax.get_xticklabels()):
#     ax.text(pos[tick], medians[tick] + .25, nobs[tick],
#             horizontalalignment='center', size='small', color='black', weight='semibold')

#Show the plot
plt.show()

#Describe (Mean and Std)
print(df.groupby("Spring_Location")['Concentration'].describe())


#Create 2 subset dataframes to compare
hawaii =df[(df['Spring_Location'] == 'Hawaii')]
alaska =df[(df['Spring_Location'] == 'Alaska')]

#Test normality
# print('Normality Test: W test statistic and P-Value')
# print(stats.shapiro(hawaii['Convert ng/g']))
# print(stats.shapiro(alaska['Convert ng/g']))
#
#
#Conduct welch's t-test
print('Welchs T-Test')
print(stats.ttest_ind(hawaii['Concentration'], alaska['Concentration'], equal_var = False))