import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')



# Reading the file

pes=pd.read_csv("C:/Users/91984/Desktop/deets-updated.csv")


# Checking the data

pes



# checking if the data contains any NULL value

pes.isnull().sum()


# Preferred foot of the players

plt.rcParams['figure.figsize'] = (10, 8)
sns.countplot(pes['foot'], palette = 'gist_rainbow')

plt.title('Preferred Foot of the Players', fontsize = 20)
plt.show()


# different positions of players 

plt.figure(figsize = (18, 10))
plt.style.use('fivethirtyeight')
ax = sns.countplot(pes['registered_position'], palette = 'plasma')
ax.set_xlabel(xlabel = 'Different Positions ', fontsize = 20)
ax.set_ylabel(ylabel = 'No: of Players', fontsize = 20)
ax.set_title(label = 'Comparison of Players and their Position', fontsize = 20)
plt.show()


# 20 youngest Players in PES

pes.sort_values('age', ascending = True)[['name', 'age', 'team_name', 'nationality','foot','overall_rating']].head(20).style.background_gradient('viridis')


# 20 Oldest players in PES

pes.sort_values('age', ascending = False)[['name', 'age', 'team_name', 'nationality','foot','overall_rating']].head(20).style.background_gradient('inferno')


# Different nations participating in PES 

plt.style.use('classic')
pes['nationality'].value_counts().head(80).plot.bar(color = 'green', figsize = (20, 7))
plt.title('Different Nations', fontsize = 30, fontweight = 20)
plt.xlabel('Name of The Country')
plt.ylabel('Total Count')
plt.show()


# best players in each position with their age, club, and nationality 

pes.iloc[pes.groupby(pes['registered_position'])['overall_rating'].idxmax()][['registered_position', 'name','age', 'team_name', 'nationality','foot','overall_rating']].style.background_gradient(cmap='YlOrRd')
