from pathlib import Path
import csv
from datetime import datetime

import plotly.express as px

# Read in data
path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Examine all fires in dataset
brightnesses, lons, lats = [], [], []
for row in reader:
    try:
        lat = float(row[header_row.index('latitude')])
        lon = float(row[header_row.index('longitude')])
        brightness = float(header_row.index('brightness'))
    except ValueError: 
        print("Missing Data")
    else:
        lats.append(lat)
        lons.append(lon)
        brightnesses.append(brightness)

title = "World Fires for 04/04/2022"
fig = px.scatter_geo(lat=lats, lon=lons, size=brightnesses, title=title,
                     color=brightnesses,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Brightness'},
                     projection='natural earth')

fig.show()