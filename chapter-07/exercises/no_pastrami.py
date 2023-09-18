sandwich_orders = ['cuban', 'pastrami', 'pastrami', 'cubano', 'blt', 'pastrami', 'tuna and mayo', 'egg and mayo']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        print(f"The Deli has run out of {current_sandwich}")
        continue
    else:
        print(f"I made your {current_sandwich}.")
        finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")