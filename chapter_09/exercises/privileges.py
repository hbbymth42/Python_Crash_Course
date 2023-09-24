from users import Users

class Privileges:

    def __init__(self, 
                 privileges=['can delete post',
                             'can add post', 
                             'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print(f"These are the privileges you have as admin:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")

class Admin(Users):

    def __init__(self, first_name, last_name, hobbies, num_pets):
        super().__init__(first_name, last_name, hobbies, num_pets)
        self.privileges = Privileges()