import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import matplotlib.dates as mdates
import seaborn as sns
from google.cloud import storage
import datetime 
from math import ceil, floor

df_trips = pd.read_csv("./blablacar_rennes_brest.csv",index_col = "Unnamed: 0") 

# Plot number of trips per day
df_trips['date_'] = pd.to_datetime(df_trips['date'], format='%Y-%m-%d')

xticks_max = ceil(df_trips.price_of_the_trip.max())
xticks_min = floor(df_trips.price_of_the_trip.min())
xticks_range = xticks_max - xticks_min

sns.set_style('darkgrid')
plt.figure(figsize=(20,12))

ax_1 = sns.distplot(df_trips.date_, bins=2*xticks_range,kde=False, rug=True)

ax_1.set_title('Number of Rennes > Brest trips', fontsize=20) 
ax_1.set_xticklabels(df_trips.date, fontsize = 15) 

ax_1.set_ylabel('Number of trips', fontsize=16)
ax_1.set_xlabel('Date', fontsize=16)

plt.show()

fig_1 = ax_1.get_figure()
fig_1.savefig('./Plots/number_of_trips_' + title_date + '.png', dpi = 160, format = 'png')


# Plot mean price per day
df_mean = df_trips.groupby(['date'])['price_of_the_trip'].mean().reset_index(name='mean_price')
df_mean['date_'] = pd.to_datetime(df_mean['date'], format='%Y-%m-%d')

sns.set_style('darkgrid')
plt.figure(figsize=(20,12))

ax_2 = sns.barplot(x="date_", y="mean_price", data = df_mean, order = df_mean["date_"].tolist())

ax_2.set_title('Rennes > Brest average price', fontsize=20) 
ax_2.set_xticklabels(df_mean.date, fontsize = 15) 

ax_2.set_ylabel('Average price', fontsize=16)
ax_2.set_xlabel('Date', fontsize=16)

plt.show()

fig_2 = ax_2.get_figure()
fig_2.savefig('./Plots/average_trip_price_' + title_date + '.png', dpi = 160, format = 'png')


# Plot median price per day
df_median = df_trips.groupby(['date'])['price_of_the_trip'].median().reset_index(name='median_price')
df_median['date_'] = pd.to_datetime(df_median['date'], format='%Y-%m-%d')

sns.set_style('darkgrid')
plt.figure(figsize=(20,12))

ax_3 = sns.barplot(x="date_", y="median_price", data = df_median, order = df_median["date_"].tolist())

ax_3.set_title('Rennes > Brest median price', fontsize=20) 
ax_3.set_xticklabels(df_median.date, fontsize = 15) 

ax_3.set_ylabel('Median price', fontsize=16)
ax_3.set_xlabel('Date', fontsize=16)

plt.show()

fig_3 = ax_3.get_figure()
fig_3.savefig('./Plots/median_trip_price_' + title_date + '.png', dpi = 160, format = 'png')


# Frequency plot
df_price_freq = df_trips.groupby(df_trips['price_of_the_trip']).size().reset_index(name='price_count')

sns.set_style('darkgrid')
plt.figure(figsize=(20,12))

ax_4 = sns.distplot(df_trips.price_of_the_trip, bins=4*xticks_range+1, kde=False, rug=True)

xticks_major = df_trips.price_of_the_trip
xticks_minor = np.linspace(xticks_min, xticks_max, 4*xticks_range+1)
xticks_minor = np.around(xticks_minor, 2)

ax_4.set_xticks(xticks_minor)  
ax_4.set_xticklabels(xticks_minor, color='#616A6B')
ax_4.set_title('Distribution of prices for Rennes > Brest trips', fontsize=20) 
ax_4.set_xlabel('Prices Rennes > Brest', fontsize=15, labelpad = 20 )
ax_4.set_ylabel('Number of trips', fontsize=15)

secax_4 = ax_4.secondary_xaxis('bottom')
secax_4.set_xticks(xticks_major) 
xticks_major_labels = np.full((len(xticks_major),), '___')
secax_4.set_xticklabels(xticks_major_labels, fontsize=12, color='#17202A')

plt.show()

fig_4 = ax_4.get_figure()
fig_4.savefig('./Plots/prices_distribution_' + title_date + '.png', dpi = 160, format = 'png')