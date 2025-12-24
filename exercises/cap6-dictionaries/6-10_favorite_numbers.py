persons_data = {
    "Alice": [3, 7, 9],
    "Bob": [2, 4, 16],
    "Charlie": [5, 6, 8, 10],
    "Diana": [1, 17, 18],
    "Ethan": [11, 12, 13],
    "Fiona": [14, 15]  
}

for person, numbers in persons_data.items():
    print(f"Los números favoritos de {person} son:")
    for number in numbers:
        print(f"- {number}")