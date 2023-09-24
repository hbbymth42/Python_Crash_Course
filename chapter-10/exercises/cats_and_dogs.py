from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        print(path.read_text())
    except FileNotFoundError:
        print(f"Sorry, file {path} was not found")
