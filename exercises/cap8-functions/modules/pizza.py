def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-pizza is about to make")
    for topping in toppings:
        print(f"- {topping}")