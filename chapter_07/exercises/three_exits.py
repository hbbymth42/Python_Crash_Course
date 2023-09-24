prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' to stop program) "
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        print("\nStopping Program")
        break
    else:
        age = int(age)
        if age < 3:
            print("Ticket Price: Free!")
            repeat = input("\nCheck another ticket price? (Y/N) ")
            if repeat.lower() == 'y':
                continue
            else:
                print("\nStopping Program")
                active = False
        elif age >= 3 and age < 12:
            print("Ticket Price: $10")
            repeat = input("\nCheck another ticket price? (Y/N) ")
            if repeat.lower() == 'y':
                continue
            else:
                print("\nStopping Program")
                active = False
        else:
            print("Ticket Price: $15")
            repeat = input("\nCheck another ticket price? (Y/N) ")
            if repeat.lower() == 'y':
                continue
            else:
                print("\nStopping Program")
                active = False