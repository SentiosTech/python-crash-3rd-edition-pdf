major_rivers = {
    'Nile': 'Africa',
    'Amazon': 'South America',
    'Yangtze': 'Asia',
    'Mississippi': 'North America',
    'Danube': 'Europe',
    'Murray': 'Australia',
}

for river in major_rivers:
    continent = major_rivers[river]
    print(f"The {river} river is located in {continent}.")
    
print("\nList of rivers:")    
for river in major_rivers.keys():
    print(river)
    
print("\nContinents where the rivers are located:")
for continent in major_rivers.values():
    print(continent)