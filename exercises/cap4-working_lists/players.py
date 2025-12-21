"""ejemplo de rebanado de listas"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("lista completa de jugadores:")
print(players)

print("\nmostrando los primeros tres jugadores:")
print(players[0:3])
print("\nmostrando tres jugadores del medio de la lista:")
print(players[1:4])
print("\nmostrando los ultimos tres jugadores:")
print(players[-3:])
print("\nmostrando todos los jugadores menos el primero:")
print(players[1:])
print("\nmostrando todos los jugadores menos el ultimo:")
print(players[:-1])
print("\nmostrando una copia de toda la lista de jugadores:")
print(players[:])
print("\nmostrando la lista en orden inverso:")
print(players[::-1]) 