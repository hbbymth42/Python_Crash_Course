from pathlib import Path
import json

path = Path('favourite_number.json')
if path.exists():
    contents = path.read_text()
    favourite_number = json.loads(contents)
    print(f"I know your favourite number! It's {favourite_number}")
else:
    favourite_number = input("What is your favourite number? ")
    contents = json.dumps(favourite_number)
    path.write_text(contents)