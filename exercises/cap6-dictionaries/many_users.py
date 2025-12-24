user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in user.items(): # recorremos el diccionario principal, obteniendo el nombre de usuario y el diccionario interno
    print(f"\nUsername: {username}") # imprimimos el nombre de usuario
    full_name = f"{user_info['first']} {user_info['last']}" # construimos el nombre completo accediendo a los valores del diccionario interno
    location = user_info['location'] # obtenemos la ubicación del usuario

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")