def make_sandwich(*toppings):
    """make a sandwich """
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('jam','lettuce','tuna','salami','onion','tomato')

