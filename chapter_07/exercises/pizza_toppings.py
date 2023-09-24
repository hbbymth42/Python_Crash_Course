prompt = "\nPlease enter a pizza topping to add to your pizza:"
prompt += "\n(Enter 'quit' when you're done) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        print("Enjoy your pizza!")
        break
    else:
        print(f"Adding {topping} to pizza!")