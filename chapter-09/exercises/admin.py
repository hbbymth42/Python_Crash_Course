class Users:

    def __init__(self, first_name, last_name, hobbies, num_pets):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies
        self.num_pets = num_pets
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\n{self.first_name.title()} " +
              f"{self.last_name.title()} has " +
              f"{self.num_pets} pets." +
              f" In their spare time, they enjoy: ")
        for hobby in self.hobbies:
            print(f"- {hobby.title()}")
    
    def greet_user(self):
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(Users):

    def __init__(self, first_name, last_name, hobbies, num_pets):
        super().__init__(first_name, last_name, hobbies, num_pets)
        self.privileges = ['can delete post', 'can add post', 'can ban user']
    
    def show_privileges(self):
        print(f"These are the privileges you have as admin:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")

admin = Admin("john", "johnson", ['tennis', 'fishing', 'playing guitar'], 0)

admin.show_privileges()