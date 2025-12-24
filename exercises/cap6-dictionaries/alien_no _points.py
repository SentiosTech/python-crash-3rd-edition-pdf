"""ejemplo de usar el método get() para acceder a valores en un diccionario, proporcionando un valor predeterminado si la clave no existe
, en lugar de generar un error, como lo haría el acceso directo, cuando la clave no está presente, como en el caso de 'points' en este ejemplo."""

alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])

point_valuee = alien_0.get('points', 'No point value assigned.') # esta funcion get() busca la clave 'points' en el diccionario alien_0 y si no la encuentra, devuelve el valor predeterminado 'No point value assigned.'
print(point_valuee)