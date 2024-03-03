# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:01:19 2024

@author: 16096
"""

import pandas as pd
import statsmodels.api as sm

# Looking at the data

wage_data = pd.read_csv('wage2.csv')
wage_data.describe()

# 1. Regression IQ on educ

X = sm.add_constant(wage_data['educ'])
y = wage_data['IQ']

model = sm.OLS(y, X).fit()

print(model.summary())

# Regression ln wage on educ

X = sm.add_constant(wage_data['educ'])
y = wage_data['lwage']

model2 = sm.OLS(y, X).fit()

print(model2.summary())

X = sm.add_constant(wage_data[['educ','IQ']])
y = wage_data['lwage']

model3 = sm.OLS(y, X).fit()

print(model3.summary())

# parents education regression

wage_data['parentseduc'] = (wage_data['meduc'] + wage_data['feduc'])/2 

X = sm.add_constant(wage_data[['educ', 'IQ', 'parentseduc']])
y = wage_data['lwage']

model4 = sm.OLS(y, X).fit()

print(model4.summary())









    











