foods = ('pizza', 'pasta', 'salad', 'soup', 'bread')
print("Original menu:")
for food in foods:
    print(f"- {food}")
# Attempting to modify the tuple will raise an error
# foods[0] = 'sushi'  # This line would cause a TypeError
# However, we can reassign the variable to a new tuple
foods = ('sushi', 'ramen', 'salad', 'soup', 'bread')
print("\nUpdated menu:")
for food in foods:
    print(f"- {food}")