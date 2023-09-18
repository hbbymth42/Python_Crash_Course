responses = {}

poll_active = True

while poll_active:
    name = input("\nWhat is your name? ")
    vacation = input("Where in the world would you like to visit? ")

    responses[name] = vacation

    repeat = input("Would someone else that would like to respond? (Yes/No) ")
    if repeat.lower() == 'no':
        poll_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")