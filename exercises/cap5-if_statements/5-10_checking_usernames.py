"""ejemplo de verificación de nombres de usuario, considerando mayúsculas y minúsculas,
ignorando diferencias entre ellas, para asegurar que los nombres de usuario sean únicos, independientemente de cómo se escriban,
en una aplicación web, utilizando listas y estructuras de control condicional."""

current_users = ['admin', 'user1', 'user2', 'user3', 'user4']

new_users = ['User1', 'user5', 'user6', 'Admin', 'user7']

for new_user in new_users:
    if new_user.lower() in (user.lower()for user in current_users):
        print(f"The username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")