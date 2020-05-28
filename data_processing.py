# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:02:30 2020

@author: Johannes Heyn
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import datetime

filename = "books_popularByDate.csv"
base_dir = "."
data_dir = "data"
fullpath = os.path.join(base_dir, data_dir, filename)


df = pd.read_csv(fullpath)
#print(df.head())
#print(df.columns)
#print(df.info())

df['pd_aux'] = pd.to_datetime(df['publish_date'], format = '%Y-%m-%d %H:%M:%S',
                              errors = 'coerce')
date_time_now = datetime.datetime.now()
age = date_time_now - df['pd_aux']
age = age.apply(lambda x: x.days)
df['age'] = age
df = df.drop('pd_aux', axis = 1)
print(df.info)

scatter = plt.figure()
ax = scatter.add_subplot(111)
ax.scatter(df['age'], df['num_ratings'])
ax.set_ylim(0, 1000000)
plt.show()

scatter = plt.figure()
ax = scatter.add_subplot(111)
ax.scatter(df['age'], df['num_reviews'])
ax.set_ylim(0, 75000)
plt.show()


print(df.loc[np.argmax(df['num_ratings'])][:])