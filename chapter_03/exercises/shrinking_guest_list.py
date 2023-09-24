guest_list = ['Leonardo Da Vinci', 'John Carmack', 'Brian Kernighan']
print(f"{guest_list[1]} cannot make it. :(")
guest_list[1] = 'Jimi Hendrix'
print("A bigger table has been found!")
guest_list.insert(0, 'Brian Eno')
guest_list.insert(2, 'Guido van Rossum')
guest_list.append('Andy Gavin')
print("... but you can only invite two guests.")
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
print(f"Hi, {guest_list[0]}, you are still invited to a special dinner!")
print(f"Ciao, {guest_list[1]}, you are still invited to a special dinner!")