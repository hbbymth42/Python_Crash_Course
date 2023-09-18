cities = {
    'tokyo': {
        'country': 'Japan',
        'population': 37_468_000,
        'fact': "Tokyo has the world's largest underground floodwater diversion facility called the Metropolitan Area Outer Underground Discharge Channel (MAOUDC).",
    },
    'delhi': {
        'country': 'India',
        'population': 28_514_000,
        'fact': "Delhi has the second-largest metropolitan area population in the world, second only to Tokyo, Japan.",
    },
    'shanghai': {
        'country': 'China',
        'population': 25_582_000,
        'fact': "Shanghai was one of the wealthiest cities in China, but also the most expensive city in mainland China to live in according to a 2017 study by the Economist Intelligence Unit.",
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    for info, description in city_info.items():
        print(f"\t{info.title()}: {description}")