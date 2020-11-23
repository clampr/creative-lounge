"""
Effect of climate change on precipitation
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# CSV columns
columns = [
    'date',
    'tavg',
    'tmin',
    'tmax',
    'prcp',
    'snow',
    'wdir',
    'wspd',
    'wpgt',
    'pres',
    'tsun'
]

# CSV file
file = 'https://bulk.meteostat.net/daily/10729.csv.gz'

# Read CSV data
df = pd.read_csv(file, compression = 'gzip', names = columns, parse_dates = { 'time': [0] }, index_col = 'time')

# Filter years and limit on summer months
time = df.index.get_level_values('time')
df = df.loc[
    (time > datetime(1949, 12, 31)) &
    (time < datetime(2020, 1, 1, 0, 0)) &
    (
        (time.map(lambda x: x.month) == 6) |
        (time.map(lambda x: x.month) == 7) |
        (time.map(lambda x: x.month) == 8)
    )
]

# Group annually and aggregate precipitation sum
df = df.groupby(pd.Grouper(freq = '1Y')).sum()

# Plot simple chart with precipitation long-term normal
df.plot(y = 'prcp', kind = 'bar', title = 'Summer Precipitation Totals')
plt.axhline(y = 210, color = 'r', linestyle = '-')
plt.show()
