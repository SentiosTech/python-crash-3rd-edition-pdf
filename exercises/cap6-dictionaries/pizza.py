# Store information about a pizza being ordered.

pizza = { # definir un diccionario para representar una pizza
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza " # acceder a un valor mediante su clave
      "with the following toppings:")
for topping in pizza['toppings']: # recorrer una lista dentro de un diccionario
    print(f"\t{topping}") 