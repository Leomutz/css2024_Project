#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:44:42 2024

@author: lm
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('movie_dataset.csv')



#print(df.info())

#print(df.describe())

#pd.set_option('display.max_rows',None)

print(df)

#remove NaN values by using mean on Revenue

x = df['Revenue (Millions)'].mean()
y = df['Metascore'].mean()
df['Revenue (Millions)'].fillna(x, inplace=True)
df['Metascore'].fillna(y, inplace=True)

#print(df.head(10))

#Average Revenue of all movies
print('Average Revenue of all movies is: ', x)

#What is the average revenue of movies from 2015 to 2017 in the dataset?

#x = df['Revenue (Millions)'].mean().
#print(df['Revenue (Millions)'].)

#print(df.loc(df['Year']>=2014) & (df['Year'] <=2017))

#print(df.loc[(df['Year'] >= 2014) & (df['Year'] <=2017)])
df1 = df.loc[(df['Year'] >= 2014) & (df['Year'] <=2017)]
#print(df1.groupby('Year'))
print(df1['Revenue (Millions)'].mean())

#How many movies were released in the year 2016? 
print(df.loc[df['Year']==2016].count())

#How many movies were directed by Christopher Nolan? 
print(df.loc[df['Director']=='Christopher Nolan'].count())

#How many movies in the dataset have a rating of at least 8.0?
print(df.loc[df['Rating']>=8.0].count())

# What is the median rating of movies directed by Christopher Nolan? 
print(df.loc[df['Director']=='Christopher Nolan'])
df2 = df.loc[df['Director']=='Christopher Nolan']
print(df2['Rating'].median())

# What is the highest rated movie in the dataset? 
#print(df.loc[lambda df['Title']: df['Rating'].max()])
#print(df['Year'].nunique())
print(df[df['Rating']==df['Rating'].max()])

#Find the year with the highest average rating? 
print(df.groupby(['Year'])['Rating'].mean())

#What is the percentage increase in number of movies made between 2006 and 2016? 
df3 = df.loc[(df['Year'] >= 2006) & (df['Year'] <=2016)]

print(df3['Votes'].pct_change())

#Find the most common actor in all the movies?
df4 = df['Actors'].mode()
print((df4))

#How many unique genres are there in the dataset?
print(df['Genre'].nunique())

#correlation of the numerical features
print(df.corr())

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),annot=True,linewidths=2)