favourite_numbers = {
    'John': [21, 215, 364],
    'Chris': [19, 34, 25, 365],
    'Ted': [27, 592, 3542, 35, 255, 23],
    'Zach': [24, 3],
    'Adam': [11, 987, 36, 25]
}

for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()}'s favourite numbers:")
    for number in numbers:
        print(f"- {number}")