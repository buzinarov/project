#save the clean data
import pandas as pd

vn_apts = pd.read_csv("vn_apts_1642_Jan_2_19_clean.csv")

#start to look at the distributions
from matplotlib import figure
import seaborn as sns
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
plt.hist(vn_apts['price'], edgecolor='black');
plt.xlabel("Price")
plt.ylabel('Count')
plt.title("Distribution of Prices");

plt.show()

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.figure(figsize=(12, 8))
sns.scatterplot(x='price', y='sqft', hue='number bedrooms', palette='summer', x_jitter=True, y_jitter=True, s=125, data=vn_apts.dropna())
plt.legend(fontsize=12)
plt.xlabel("Price", fontsize=18)
plt.ylabel("Square Footage", fontsize=18);
plt.title("Price vs. Square Footage Colored by Number of Bedrooms", fontsize=18);
plt.show()

plt.figure(figsize=(12, 8))
sns.regplot(x='price', y='sqft', data=vn_apts.dropna());
plt.title('Price vs. Square Footage Regression Plot');
plt.xlabel("Price (CAD)");
plt.ylabel("Square Feet");

plt.show()

vn_apts.corr()



#group by neighborhood
vn_apts.groupby('neighborhood').mean()

vn_apts['neighborhood'].replace('North Oakland', 'Oakland North', inplace=True)

#sort price to find cheapest
vn_apts.groupby('neighborhood').mean()['price'].sort_values()

plt.figure(figsize=(15,10))
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)


sns.boxplot(x='neighborhood', y='price', data=vn_apts)
plt.xlabel("Neighborhood");
plt.xticks(rotation=75)
plt.ylabel("Price CAD");
plt.title("Prices by Neighborhood - Boxplots");

plt.show()