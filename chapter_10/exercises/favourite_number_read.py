from pathlib import Path
import json

path = Path('favourite_number.json')
contents = path.read_text()
favourite_number = json.loads(contents)

print(f"I know your favourite number! It's {favourite_number}")