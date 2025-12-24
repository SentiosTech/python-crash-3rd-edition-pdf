"""ejemplo de uso de una declaración if para verificar si un usuario está en una lista de usuarios prohibidos."""

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")