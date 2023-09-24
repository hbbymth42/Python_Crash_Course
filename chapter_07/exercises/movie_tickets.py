prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' to stop program) "
while True:
    age = input(prompt)

    if age == 'quit':
        print("Stopping Program")
        break
    else:
        age = int(age)
        if age < 3:
            print("Ticket Price: Free!")
        elif age >= 3 and age < 12:
            print("Ticket Price: $10")
        else:
            print("Ticket Price: $15")