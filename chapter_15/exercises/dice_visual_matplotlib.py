import matplotlib.pyplot as plt

from die import Die

# Create two D6 Dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyse the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Visualise the results
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15,9))
ax.bar(poss_results, frequencies)
ax.set_title("Results of Rolling Two D6 Dice 1,000 times", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)
ax.set_xticks(poss_results)

plt.show()