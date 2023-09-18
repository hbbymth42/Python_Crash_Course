favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

polling_list = ['phil', 'sarah', 'erin', 'john', 'chris', 'zach']

for name in sorted(polling_list):
    if name in favourite_languages.keys():
        print(f"\nThank you for responding {name.title()}!")
    else:
        print(f"\nWe would like to invite you to do our Favourite Languages poll {name.title()}!")