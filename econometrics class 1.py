

import pandas as pd

auto_data = pd.read_csv('auto.csv')

print(auto_data[["price", "weight", "mpg", "length"]].describe())

auto_data['gpm'] = 1/auto_data['mpg']
print(auto_data[['gpm', 'mpg']].describe())

print('Calculated by hand:' , 1/21.29729)
print('Calculated by hand' , 1/auto_data['mpg'].mean())

import matplotlib.pyplot as plt

plt.scatter(auto_data['weight'], auto_data['mpg'])

plt.title('Scatter plot of weight and mpg')
plt.xlabel('Weight')
plt.ylabel('MPG')

print(auto_data[['mpg', 'weight']].corr())

foreign_car = auto_data[auto_data['foreign'] == 'Foreign']
domestic_car = auto_data[auto_data['domestic'] == 'Domestic']

print('The average price of foreign cars:', foreign_car['price'].mean())


X = sm.add_constant(auto_data['weight'])
Y = auto_data['mpg']

model1 = sm.OLS(y, X).fit()

print(model.summary())




