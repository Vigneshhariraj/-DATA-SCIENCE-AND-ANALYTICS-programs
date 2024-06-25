import numpy as np 
import pandas as pd 
import matplotlib 
from matplotlib import pyplot as plt 
import seaborn as sns 

# Load time series dataset
df_power = pd.read_csv("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")
print(df_power.columns) 
print(df_power.shape) 
print(df_power.tail(10)) 
print(df_power.dtypes) 

# Convert 'Date' column to datetime format
df_power['Date'] = pd.to_datetime(df_power['Date'])
print(df_power.dtypes) 

# Set 'Date' as the index
df_power = df_power.set_index('Date') 
print(df_power.tail(3)) 
print(df_power.index) 

# Add columns with year, month, and weekday name
df_power['Year'] = df_power.index.year 
df_power['Month'] = df_power.index.month_name() 
df_power['Weekday_Name'] = df_power.index.day_name() 

# Display a random sampling of 5 rows
print(df_power.sample(5, random_state=0)) 

# Generate a line plot of Germany's daily electricity consumption
print(df_power.loc['2015-10-02']) 
sns.set(rc={'figure.figsize': (11, 4)}) 
plt.rcParams['figure.figsize'] = (8, 5) 
plt.rcParams['figure.dpi'] = 100 

df_power['Consumption'].plot(linewidth=0.5) 
plt.title('Daily Electricity Consumption (GWh)')
plt.ylabel('Consumption (GWh)')
plt.show() 

# Plot data for all columns
cols_to_plot = ['Consumption', 'Solar', 'Wind'] 
axes = df_power[cols_to_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(14, 6), subplots=True) 
for ax in axes: 
    ax.set_ylabel('Daily Totals (GWh)') 
plt.show() 

# Investigate a single year
ax = df_power.loc['2016', 'Consumption'].plot() 
ax.set_ylabel('Daily Consumption (GWh)') 
ax.set_title('Daily Electricity Consumption in 2016')
plt.show() 

# Examine December 2016
ax = df_power.loc['2016-12', 'Consumption'].plot(marker='o', linestyle='-') 
ax.set_ylabel('Daily Consumption (GWh)') 
ax.set_title('Daily Electricity Consumption in December 2016')
plt.show() 

# Consumption in a specific week of December
ax = df_power.loc['2016-12-23':'2016-12-30', 'Consumption'].plot(marker='o', linestyle='-') 
ax.set_ylabel('Daily Consumption (GWh)') 
ax.set_title('Daily Electricity Consumption from 2016-12-23 to 2016-12-30')
plt.show() 

# Group the data by months and visualize with box plots
fig, axes = plt.subplots(3, 1, figsize=(8, 7), sharex=True) 
for name, ax in zip(['Consumption', 'Solar', 'Wind'], axes): 
    sns.boxplot(data=df_power, x='Month', y=name, ax=ax) 
    ax.set_ylabel('GWh') 
    ax.set_title(name) 
    if ax != axes[-1]: 
        ax.set_xlabel('') 
plt.show() 

# Group the consumption by day of the week with a box plot
sns.boxplot(data=df_power, x='Weekday_Name', y='Consumption') 
plt.title('Daily Electricity Consumption by Weekday')
plt.ylabel('Consumption (GWh)')
plt.xlabel('Weekday')
plt.show() 

# Resample data
columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar'] 
power_weekly_mean = df_power[columns].resample('W').mean() 
print(power_weekly_mean.tail(10)) 

# Plot the last six months of 2016
start, end = '2016-01', '2016-06' 
fig, ax = plt.subplots() 
ax.plot(df_power.loc[start:end, 'Solar'], marker='.', linestyle='-', linewidth=0.5, label='Daily') 
ax.plot(power_weekly_mean.loc[start:end, 'Solar'], marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample') 
ax.set_ylabel('Solar Production (GWh)') 
ax.set_title('Solar Production: Daily vs. Weekly Mean')
ax.legend() 
plt.show()
