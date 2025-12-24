data = {
    'dog': {
        'type': 'canine',
        'owner': 'Alice',
        'age': 5
    },
    'cat': {
        'type': 'feline',
        'owner': 'Bob',
        'age': 3
    },
    'parrot': {
        'type': 'avian',
        'owner': 'Charlie',
        'age': 2
    },
    
    'fish': {
        'type': 'aquatic',
        'owner': 'Diana',
        'age': 1
    }
}


petes = ['dog', 'cat', 'parrot', 'fish']

for pet in petes:
    print(f"\nInformation about the {pet.title()}:")
    pet_info = data[pet]
    pet_type = pet_info['type']
    owner = pet_info['owner']
    age = pet_info['age']
    
    print(f"\tType: {pet_type.title()}")
    print(f"\tOwner: {owner}")
    print(f"\tAge: {age} years old")
# Otra forma de recorrer el diccionario anidado
print("\n" + "="*40)
print("\nDetailed Information of all Pets:")
for pet, pet_info in data.items():
    print(f"\nDetails of {pet.title()}:")
    for key, value in pet_info.items():
        print(f"\t{key.title()}: {value}")