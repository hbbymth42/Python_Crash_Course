sandwich_orders = ['cuban', 'cubano', 'blt', 'tuna and mayo', 'egg and mayo']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")