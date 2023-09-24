from pathlib import Path
import json

favourite_number = input("What is your favourite number? ")

path = Path('favourite_number.json')
contents = json.dumps(favourite_number)
path.write_text(contents)