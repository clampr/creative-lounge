"""
Reading CSV Data with Pandas
"""

import pandas as pd
import matplotlib.pyplot as plt

# CSV Columns
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

# The CSV file
file = 'https://bulk.meteostat.net/daily/10729.csv.gz'

# Read CSV data
df = pd.read_csv(file, compression = 'gzip', names = columns, parse_dates = { 'time': [0] }, index_col = 'time')

# Describe the DataFrame
print(df.head())

# Plot a simple chart
#df.plot(y = 'tavg', kind = 'line')
#plt.show()
