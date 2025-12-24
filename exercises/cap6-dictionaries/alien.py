"""ejemplo de un diccionario para representar un alienígena, con dos pares clave-valor,
uno para el color y otro para los puntos que vale al ser derribado, y luego imprime ambos valores,
uno por línea, usando sus claves."""
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

"""agrega un par clave-valor al diccionario alien_0 para almacenar la posición x e y del alienígena,
luego imprime el diccionario completo."""

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

"""empezar con diccionario vacio y luego agregar pares clave-valor."""

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

"""modificar valores en un diccionario."""
alien_3 = {'color': 'green', 'points': 5}
print(f"The alien is {alien_3['color']}.")

alien_3['color'] = 'yellow'
print(f"The alien is now {alien_3['color']}.")
