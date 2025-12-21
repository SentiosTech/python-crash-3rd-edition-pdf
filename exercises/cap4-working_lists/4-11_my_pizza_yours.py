pizzas = ['pepperoni', 'margherita', 'hawaiian', 'bbq chicken', 'veggie', 'meat lovers', 'four cheese', 'supreme']
friends_pizzas = pizzas[:]  # Create a copy of the list
pizzas.append('buffalo chicken')
friends_pizzas.append('pesto')
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")
    
print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"- {pizza}")