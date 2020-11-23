"""
Spatial sampling with Meteostat
"""

from meteostat import Stations, Daily
from datetime import datetime
import matplotlib.pyplot as plt

# Get 20 random weather stations in Germany
stations = Stations(country = 'DE', daily = datetime(2005, 1, 1)).fetch(limit = 20, sample = True)

# Get daily data
data = Daily(stations, max_threads = 5, start = datetime(1980, 1, 1), end = datetime(2019, 12, 31))

# Normalize data and aggregate
data = data.normalize().aggregate(freq = '5Y', spatial = True).fetch()

# Plot chart
data.plot(y = ['tavg'], kind = 'line', title = 'Sampled DE Annual Mean Temperature from 1980 to 2019')
plt.show()
