"""
Are there more storms because of climate change?
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

# Filter years
time = df.index.get_level_values('time')
df = df.loc[
    (time > datetime(1969, 12, 31)) &
    (time < datetime(2020, 1, 1, 0, 0))
]

# Get annual count of peak wind gusts > 75 km/h
df = df[df['wpgt'] >= 75]['wpgt'].groupby(pd.Grouper(freq = '1Y')).count()

# Plot simple chart
df.plot(y = 'wpgt', kind = 'line', title = 'Annual Count of Wind Gusts >= 75 km/h')
plt.show()
