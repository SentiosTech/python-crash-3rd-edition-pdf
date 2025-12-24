person_data1 = {
    'first_name': 'ada',
    'last_name': 'lovelace',
    'age': 28,
    'city': 'london',
}

person_data2 = {
    'first_name': 'alan',
    'last_name': 'turing',
    'age': 41,
    'city': 'manchester',
}

person_data3 = {
    'first_name': 'grace',
    'last_name': 'hopper',
    'age': 85,
    'city': 'new york',
}
people = [person_data1, person_data2, person_data3] # lista que contiene los diccionarios de cada persona

for person in people: # recorremos la lista de personas
    print("\nPerson Information:") # encabezado para la información de la persona
    full_name = f"{person['first_name']} {person['last_name']}" # construimos el nombre completo
    age = person['age'] # obtenemos la edad
    city = person['city'] # obtenemos la ciudad

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tAge: {age}")
    print(f"\tCity: {city.title()}")
    
