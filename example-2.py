"""
Aggregating Data with Pandas
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

# Remove current year
#time = df.index.get_level_values('time')
#df = df.loc[time < datetime(2020, 1, 1, 0, 0)]

# Group by year and aggregate mean
df = df.groupby(pd.Grouper(freq = '1Y')).mean()
# 1Y -> 10Y for trend

# Plot simple chart
df.plot(y = 'tavg', kind = 'line', title = 'Annual Mean Temperature')
plt.show()
