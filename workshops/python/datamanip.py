#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 09:52:49 2018

@author: cag3fr
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.figure()

help(pd.read_csv)

df = pd.read_csv('us-census-demographic-data/acs2015_county_Data.csv')
type(df)

# Dimensions
df.shape
# Rows
df.index
# columns
df.columns
# Number of rows
len(df.index)
# Number of columns
len(df.columns)

# Viewing with head and tail
df.head()
df.head(n=20)
df.tail()

# Summary stats
df.describe()

## filtering
df.State == "Virginia"
df[df.State == "Virginia"]
df.query("State == 'Virginia'")
dfVA = df[df.State=="Virginia"]
df[df.TotalPop >= 100000]
df[(df.State == "Virginia") & (df.TotalPop >= 100000)]
df[(df.State == "Virginia") | (df.State == "Maryland")]
df.query("State == 'Ohio' & SelfEmployed > 8.0")

# Example
# Find the counties that have a total population greater than 200000 and an
# unemployment rate less than or equal to 5%.
# Should be 16 rows by 37 columns
df[(df.TotalPop>200000) & (df.Unemployment<=5)]

# quantiles
df.Income.quantile(0.99)
df[df.Income > 87745.4]
df[df.Income > df.Income.quantile(0.99)]

# Example
# Find the rows that are in 90th percentile for the Total Population 
df[df.TotalPop > df.TotalPop.quantile(0.90)]
df.query("TotalPop > TotalPop.quantile(0.90)")
# histogram
df.Income.hist()

# Selecting data
df[["TotalPop"]]
df[["TotalPop","Men","Women"]]
df.drop("CensusId",axis=1)
df.loc[:,"State":"Women"]

# sort
df.sort_values(by="TotalPop")
df.sort_values(by="State", ascending=False)

# Select and sort
df[["State","County","TotalPop"]].sort_values(by="TotalPop")

# example
df[["State", "County", "Income"]].sort_values(by="Income",ascending=False)


# assign
myDF = df.loc[:,"State":"Women"]
myDF.assign(MFratio=df.Men/df.Women)
myDF.assign(MFratio=df.Men/df.Women, PMen=df.Men/df.TotalPop, PWomen=df.Women/df.TotalPop)

# groupby
df.groupby("State")
df.groupby("State").describe()
df.groupby("State").agg({"MeanPopulation": "mean"})
df.groupby("State").agg([np.mean,np.std])
df.groupby("State").Employed.sum()
df.groupby("State").Employed.sum().reset_index().sort_values(by = "Employed")
# Example
df.groupby("State").Income.agg("median")

# Example
# Filter by the State of California and Total Population Greater Than 200000.
# Sort by Unemployment Rate in Descending Order and View the First 10 rows
df[(df.State == "California") & (df.TotalPop > 200000)].sort_values(by="Unemployment", ascending=False).head(n=10)
df.query("State == 'California' & TotalPop > 200000").sort_values(by="Unemployment", ascending=False).head(n=10)

# Piping
(df
     .query("State == 'California' & TotalPop > 200000")
     .sort_values(by="Unemployment", ascending=False)
     .head(n=10)
     )

(df[(df.State == "California") & (df.TotalPop > 200000)]
     .sort_values(by="Unemployment", ascending=False)
     .head(n=10)
     )

(df
     [["State", "TotalPop"]]
     .groupby("State")
     .agg(np.median)
     .hist()
     )

# Write to Output
myDF.to_csv("output.csv")

# More Examples
# 6
(df
     .groupby("State")
     .SelfEmployed
     .describe()
     .tail()
     )

# 7
(df
     [["State","County","TotalPop","Citizen"]]
     .assign(PCitizen = df.Citizen/df.TotalPop)
     .query("State == 'Alaska' | State == 'Hawaii'")    
     .sort_values(by = "PCitizen")
     .head(n = 10)
)

# 8
(df
     .query("White <= 50")
     .groupby("State")
     .agg({"Income": "median"})
     )

# 9
(df
     .groupby("State")
     .agg({"MeanCommute": "mean"})
     .reset_index()
     .sort_values(by = "MeanCommute", ascending=False)
     .head()
     )
