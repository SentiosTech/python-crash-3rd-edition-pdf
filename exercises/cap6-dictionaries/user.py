"""ejemplo de recorrido de un diccionario con un ciclo for """
user_0 = { # un diccionario con información de un usuario
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key , value in user_0.items(): # recorremos el diccionario con un ciclo for, usando el método items(), que devuelve pares clave-valor
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
