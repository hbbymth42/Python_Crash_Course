from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/honolulu_weather_2019_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and rainfall.
dates, rainfall = [], []
for row in reader:
    current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
    try:
        current_rainfall = float(row[header_row.index('PRCP')])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfall.append(current_rainfall)

# Plot rainfall.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='blue')

# Format plot.
ax.set_title("Daily Rainfall, 2019\nHonolulu, HI", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()