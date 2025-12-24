persons_data = {
    "Alice": [3],
    "Bob": [2],
    "Charlie": [5],
    "Diana": [1],
    "Ethan": [11],
    "Fiona": [14]  
}

for person, numbers in persons_data.items():
    print(f"El número favorito de {person} es:")
    for number in numbers:
        print(f"- {number}")