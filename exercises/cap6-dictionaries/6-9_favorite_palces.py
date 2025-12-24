favorite_places = {
    'alice': ['paris', 'new york'],
    'bob': ['tokyo', 'seoul', 'beijing'],
    'carol': ['london', 'berlin', 'rome'],
    'dave': ['sydney', 'melbourne', 'brisbane'],
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
    print()  # Add a blank line for better readability between persons