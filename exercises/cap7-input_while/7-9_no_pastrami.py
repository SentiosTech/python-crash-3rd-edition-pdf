sandwich_orders = [
    "Club Sandwich",
    "Pastrami on Rye",
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
    "Pastrami on Rye",
    "Steak Sandwich",
    "Chicken Caesar Wrap",
    "Tuna Melt",
    "Sloppy Joe",
    "Pastrami on Rye",
    "Buffalo Chicken"]

print("the deli has run out of pastrami")
print(f"original:", sandwich_orders)
while 'Pastrami on Rye' in sandwich_orders:
    sandwich_orders.remove('Pastrami on Rye')
    
print(f"\nactual:",sandwich_orders)