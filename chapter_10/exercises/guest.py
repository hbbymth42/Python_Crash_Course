from pathlib import Path

guest = input("Enter your name: ")

path = Path('guest.txt')

path.write_text(guest)