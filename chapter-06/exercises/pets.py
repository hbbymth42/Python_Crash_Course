polly = {
    'name': 'polly',
    'owner name': 'john',
    'kind': 'parrot'
}

barry = {
    'name': 'barry',
    'owner name': 'erin',
    'kind': 'dog'
}

zophie = {
    'name': 'zophie',
    'owner name': 'al',
    'kind': 'cat',
}

pets = [polly, barry, zophie]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
    print("\n")