class Users:

    def __init__(self, first_name, last_name, hobbies, num_pets):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies
        self.num_pets = num_pets
    
    def describe_user(self):
        print(f"\n{self.first_name.title()} " +
              f"{self.last_name.title()} has " +
              f"{self.num_pets} pets." +
              f" In their spare time, they enjoy: ")
        for hobby in self.hobbies:
            print(f"- {hobby.title()}")
    
    def greet_user(self):
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}!")
