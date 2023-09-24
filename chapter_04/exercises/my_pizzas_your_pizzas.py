my_pizzas = ['pepperoni', 'chicken', 'garlic']
friend_pizzas = my_pizzas[:]

my_pizzas.append('meatlovers')
friend_pizzas.append('hawaiian')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)