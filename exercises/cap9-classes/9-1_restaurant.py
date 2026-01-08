class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"My restaurant name is {self.restaurant_name}.")
        print(f"My cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

# crear una instancia
restaurant = Restaurant('Milk', 'coffee')
print(restaurant)
# imprimir atributos individualmente
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# llamar a los metodos
restaurant.describe_restaurant()
restaurant.open_restaurant()
