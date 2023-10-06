import plotly.express as px

from die import Die

# Create two D6s.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyse the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results
title = "Multiplying Results of Rolling three D6 dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customise chart.
fig.update_layout(xaxis_dtick=1)
fig.show()