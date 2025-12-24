"""ejemloplo de una lista de diccionarios"""

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
print("\n--- Creando 30 aliens verdes ---")
# crear una lista vacía para almacenar los aliens
aliens = []

# crear 30 aliens verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
# modificar los primeros 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
 # modificar el siguiente alien
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
    
# mostrar los primeros 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")  # indicar que hay más aliens

# mostrar el número total de aliens creados
print(f"Número total de aliens: {len(aliens)}")
