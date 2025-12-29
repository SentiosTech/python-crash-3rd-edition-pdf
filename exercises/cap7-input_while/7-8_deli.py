sandwich_orders = [
    "Club Sandwich",
    "BLT (Bacon, Lettuce, Tomato)",
    "Chicken Salad Sandwich", 
    "Turkey and Swiss",
    "Roast Beef with Horseradish",
    "Ham and Cheese",
    "Pastrami on Rye",
    "Philly Cheesesteak",
    "Italian Sub",
    "Meatball Marinara",
    "Chicken Parmesan",
    "Pulled Pork BBQ",
    "Cuban Sandwich",
    "Reuben Sandwich",
    "Steak Sandwich",
    "Chicken Caesar Wrap",
    "Tuna Melt",
    "Sloppy Joe",
    "Monte Cristo",
    "Buffalo Chicken"]

finished_sandwiches = []
 # sandwich_orders lista 
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"i making your {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)
    
print("\nThe following sandwich orders have been confirmed:")
for finished_sandwich in finished_sandwiches:
    print(f"IT IS MADE OF {finished_sandwich.upper()}")
    