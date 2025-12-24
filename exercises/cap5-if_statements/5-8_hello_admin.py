"""ejemplo de uso de declaraciones if para saludar a usuarios
con un mensaje especial para el administrador, y un mensaje general para otros usuarios,
utilizando una lista de nombres de usuario predefinida,
y recorriéndola con un bucle for, para imprimir el saludo correspondiente a cada usuario,
dependiendo de si es el administrador o no, utilizando f-strings para formatear los mensajes."""

usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")