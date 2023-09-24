guest_list = ['Leonardo Da Vinci', 'John Carmack', 'Brian Kernighan']
print(f"{guest_list[1]} cannot make it. :(")
guest_list[1] = 'Jimi Hendrix'
print("A bigger table has been found! We can invite more guests!")
guest_list.insert(0, 'Brian Eno')
guest_list.insert(2, 'Guido van Rossum')
guest_list.append('Andy Gavin')
print(f"Hi, {guest_list[0]}, you are invited to a special dinner!")
print(f"Ciao, {guest_list[1]}, you have been invited to a special dinner!")
print(f"Hello, {guest_list[2]}, you are invited to a special dinner!")
print(f"Good day, {guest_list[3]}, this is a special invitation to a special dinner!")
print(f"Greetings, {guest_list[4]}, you have been invited to a special dinner!")
print(f"Good News {guest_list[5]}! You have been invited to a special dinner!")