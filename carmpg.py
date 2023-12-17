# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:53:34 2015

@author: nymph
"""


#################################### Read the data ############################
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

''' read_csv()
The read_csv() function in pandas package parse an csv data as a DataFrame data structure. What's the endpoint of the data?
The data structure is able to deal with complex table data whose attributes are of all data types. 
Row names, column names in the dataframe can be used to index data.
'''

data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original", delim_whitespace = True, \
header=None, names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model', 'origin', 'car_name'])

data['mpg']
data.mpg
data.iloc[0,:]

print(data.shape)

################################## Enter your code below ######################

#1. How many cars and how many attributes are in the data set.
num_cars = len(data)
num_attributes = len(data.columns)
print("Number of cars: ", num_cars)
print("Number of attributes: ", num_attributes)

print('\n')
# 2. How many distinct car companies are represented in the data set? What is the name of the car
# with the best MPG? What car company produced the most 8-cylinder cars? What are the names
# of 3-cylinder cars? Do some internet search that can tell you about the history and popularity of
# those 3-cylinder cars

num_companies = len(data['car_name'].str.split().str[0].unique())
print("Number of distinct car companies: ", num_companies)
best_mpg_car = data.loc[data['mpg'].idxmax()]['car_name']
print("Car with the best MPG: ", best_mpg_car)
most_8cyl_company = data.loc[data['cylinders'] == 8]['car_name'].str.split().str[0].mode()[0]
print("Car company that produced the most 8-cylinder cars: ", most_8cyl_company)
cyl3_cars = data.loc[data['cylinders'] == 3]['car_name'].unique()
print("Names of 3-cylinder cars: ", cyl3_cars)

print('\n')

# 3. What is the range, mean, and standard deviation of each attribute? Pay attention to potential missing values
desc_stats = data.describe()

# Print the range, mean, and standard deviation of each attribute
for col in desc_stats.columns:
    if col != 'count':
        range = desc_stats[col]['max'] - desc_stats[col]['min']
        mean = desc_stats[col]['mean']
        standard_deviation = desc_stats[col]['std']

        print(f"{col}:")
        print(f"    Range: {range}")
        print(f"    Mean: {mean}")
        print(f"    Standard deviation: {standard_deviation}\n")

#4. Plot histograms for each attribute. Pay attention to the appropriate choice of number of bins.
#Write 2-3 sentences summarizing some interesting aspects of the data by looking at the histograms.
data.hist(bins=20, figsize=(10, 8))
plt.suptitle('Histograms of Auto MPG Data Attributes')
plt.show()
print("The cylinders attribute is heavily skewed towards 4 and 8 cylinder cars, with relatively few 3 and 5 cylinder cars.")
print("The horsepower attribute is also skewed, with a large number of cars having low horsepower and a long tail to the right.")
print('\n')

#5. Plot a scatterplot of weight vs. MPG attributes. What do you conclude about the relationship
#between the attributes? What is the correlation coefficient between the 2 attributes?

plt.scatter(data['weight'], data['mpg'])
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.title('Scatterplot of Weight vs. MPG')
plt.show()
print("As for the relationship between the attributes and the correlation coefficient, we can see from the scatterplot that there seems to be a negative correlation between weight and MPG, meaning that as weight increases, MPG tends to decrease.")
print('\n')
print(data[['weight','mpg']].corr())
# 6. Plot a scatterplot of year vs. cylinders attributes. Add a small random noise to the values to make
# the scatterplot look nicer. What can you conclude? Do some internet search about the history of car
# industry during 70’s that might explain the results.(Hint: data.mpg + np.random.random(len(data.mpg))
# will add small random noise)

plt.scatter(data=data, x="model", y="cylinders");
plt.title('Scatterplot of year vs. cylinders attributes')
plt.show()

noise = data.mpg + np.random.random(len(data.mpg))
data1 = data.copy()
data1['model'] += noise
data1['cylinders'] += noise
plt.scatter(data=data1, x="model", y="cylinders");
plt.title('Scatterplot of year vs. cylinders attributes (Random noise)')
plt.show()

print("From the scatterplot, we can see that the number of cylinders in cars decreased over time from the 1970s to the early 1980s")
print("According to what i search on the internet,In 1970 the American automobile industry was under threat from several angles. Falling sales, a 57-day strike at General Motors idling around 347,000 workers, and higher quality foreign cars were the primary culprits, oil crisis,  which led to increased demand for more fuel-efficient cars. As a result, many car manufacturers began to reduce the number of cylinders in their cars to improve fuel efficiency.")
print('\n')
#7.  Show 2 more scatterplots that are interesting do you. Discuss what you see.

#Displacement vs MPG
plt.scatter(data['displacement'], data['mpg'], alpha=0.5)
plt.xlabel('Displacement')
plt.ylabel('MPG')
plt.title('Displacement vs. MPG')
plt.show()
print("Displacement vs. MPG: This scatterplot can show the relationship between the size of the engine and the fuel efficiency of the car. It can be expected that larger engines consume more fuel and therefore have lower MPG.")

#Weight vs acceleration
plt.scatter(data['weight'], data['acceleration'], alpha=0.5)
plt.xlabel('Weight')
plt.ylabel('Acceleration')
plt.title('Weight vs. Acceleration')
plt.show()
print("Weight vs. Acceleration: This scatterplot can show the relationship between the weight of the car and how quickly it can accelerate. It can be expected that heavier cars have slower acceleration times.")
print('\n')
# 8. Plot a time series for all the companies that show how many new cars they introduces during
#each year. Do you see some interesting trends? (Hint: data.car name.str.split()[0] returns
#a vector of the first word of car name column.)

data['company'] = data['car_name'].str.split().str[0]
new_cars_by_company = data.groupby(['company', 'model'])['car_name'].count()
fig, ax = plt.subplots(figsize=(15, 7))
for company in new_cars_by_company.index.get_level_values('company').unique():
    new_cars_by_company.loc[company].plot(ax=ax, label=company)
ax.set_title('Number of New Cars Introduced by Company over year')
ax.legend()
plt.show()

print("Firstly, there is a clear decline in the number of new cars introduced by American companies from the 1970s to the 1980s.")
print("Secondly, Japanese car companies such as Toyota, Nissan and Honda showed a steady increase in the number of new cars introduced during this time period")
print("Thirdly, European car companies such as Volkswagen, Volvo and BMW showed fluctuations in the number of new cars introduced")
print('\n')
# 9. Calculate the pairwise correlation, and draw the heatmap with Matplotlib. Do you see some
# interesting correlation? (Hint: data.iloc[:,0:8].corr(), plt.pcolor() draws the heatmap.)

corr_matrix = data.iloc[:,0:8].corr()
plt.pcolor(corr_matrix, cmap='RdBu')
plt.colorbar()
plt.xticks(np.arange(0.5, len(corr_matrix.columns), 1), corr_matrix.columns, rotation=90)
plt.yticks(np.arange(0.5, len(corr_matrix.index), 1), corr_matrix.index)
plt.show()

print("Yes. There are some interesting correlations\n")
print("Strong positive correlation between horsepower and weight of the car.")
print("Strong negative correlation between miles per gallon (mpg) and both horsepower and weight.")
print("Positive correlation between displacement and horsepower, as well as between displacement and weight.")
print("Negative correlation between mpg and acceleration.")