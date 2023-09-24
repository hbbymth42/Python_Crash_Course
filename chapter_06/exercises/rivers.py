rivers = {
    'nile': 'egypt',
    'mississippi': 'united states of america',
    'thames': 'england'
}

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(f"\n{river.title()} River")

for country in rivers.values():
    print(f"\n{country.title()}")