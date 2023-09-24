from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_user(path):
    """Prompt for a new username."""
    user = {}
    user['name'] = input("What is your name? ")
    user['age'] = input("How old are you? ")
    user['favourite_number'] = input("Favourite Number? ")
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_username(path)
    return_user = input(f"Is {user['name']} your user name? (Y/N)")
    if return_user.lower() == 'y':
        print(f"Welcome back, {user['name']}!")
        print(f"\nYou are {user['age']} years old.")
        print(f"\nYour favourite number is {user['favourite_number']}")
    else:
        print("\nSeems like we have a new user, welcome!")
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['name']}!")
    
greet_user()