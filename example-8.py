"""
How the Atlantic causes mild winters in Europe
"""

from meteostat import Stations, Daily
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Get weather stations by Meteostat ID
stations = Stations(id = ['D1424', '10729', '10803', '10513']).fetch()

# Get daily data since 1980
data = Daily(stations, max_threads = 5, start = datetime(1980, 1, 1), end = datetime(2019, 12, 31))

# Normalize data
data = data.normalize().fetch()

# Function for converting degrees to Boolean (North-East or Not-North-East)
def direction(value):
    if (value >= 337 and value <= 360) or value <= 114:
        return 1
    else:
        return 0

# Convert wind direction
data['wdir'] = data['wdir'].apply(direction)

# Filter for DEC and JAN only
time = data.index.get_level_values('time')
data = data.loc[
    (
        (time.map(lambda x: x.month) == 12) |
        (time.map(lambda x: x.month) == 1)
    )
]

# Group annually and aggregate
data = data.groupby(pd.Grouper(level = 'time', freq = '1Y')).agg({ 'wdir': 'sum', 'tavg': 'mean'})

# Create chart
fig, ax = plt.subplots(figsize = (8, 6))

# Wind data
ax.set_ylabel('Days with North-East Wind', color = 'tab:blue')
data['wdir'].plot(kind = 'line', ax = ax, color = 'tab:blue', title = 'Correlation between North-East Wind and Low Mean Temperature in DE (DEC & JAN)')

# Mean Temperature data
ax2 = ax.twinx()
ax2.set_ylabel('Mean Temperature (°C)', color = 'tab:red')
data['tavg'].plot(kind = 'line', ax = ax2, color = 'tab:red')

# Show chart
plt.show()
