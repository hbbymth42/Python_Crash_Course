hobbymath42 = {
    'full name': 'hobby math',
    'age': 42,
    'city': 'honolulu',
}

test_user12 = {
    'full name': 'john smith',
    'favourite programming language': 'c',
    }

another_user21 = {
    'full name': 'erin smith',
    'number of pets': 3,
}
people = [hobbymath42, test_user12, another_user21]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("\n")