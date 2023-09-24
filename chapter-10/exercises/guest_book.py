from pathlib import Path

contents = ''
while True:
    user = input("Enter your name (Enter 'q' to quit): ")
    if user == 'q':
        break
    contents += f"{user}\n"

path = Path('guest_book.txt')
path.write_text(contents)
    