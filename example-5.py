"""
Do we see less snow due to climate change?
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
    (time > datetime(1990, 12, 31)) &
    (time < datetime(2020, 1, 1, 0, 0))
]

# Function for converting mm to cm
def mm_to_cm(value):
    return value / 10

# Group annually, get snow cover maximum and convert to cm
df = df['snow'].groupby(pd.Grouper(freq = '1Y')).max().apply(mm_to_cm)

# Plot simple chart
df.plot(kind = 'line', title = 'Annual Max. Snow Cover in Mannheim')
plt.show()
