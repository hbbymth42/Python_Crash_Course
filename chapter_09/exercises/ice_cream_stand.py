class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves " + 
              f"{self.cuisine_type.title()} cuisine")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, num_served):
        self.number_served += num_served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['chocolate', 'strawberry', 'vanilla']

my_ice_cream_stand = IceCreamStand('test', 'italian')
print(my_ice_cream_stand.flavours)