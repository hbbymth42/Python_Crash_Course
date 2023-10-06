from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and rainfall.
dates, rainfall = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    current_rainfall = float(row[5])
    dates.append(current_date)
    rainfall.append(current_rainfall)

# Plot rainfall.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='blue')

# Format plot.
ax.set_title("Daily Rainfall, 2019\nSitka, AL", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()