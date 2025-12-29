dinner_groups = input("How many people are in your dinner group? ")
dinner_groups = int(dinner_groups)

if dinner_groups > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")
