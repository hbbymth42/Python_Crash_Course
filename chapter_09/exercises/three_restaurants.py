class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves " + 
              f"{self.cuisine_type.title()} cuisine")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

restaurant_1 = Restaurant("tgi fridays", "american")
restaurant_2 = Restaurant("mcdonalds", "fast food")
restaurant_3 = Restaurant("panda express", "chinese")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
