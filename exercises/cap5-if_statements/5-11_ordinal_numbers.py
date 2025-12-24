"""ejemplo de generación de números ordinales en inglés, utilizando estructuras de control condicional para asignar los sufijos correctos a cada número,
y mostrando el resultado en la consola."""

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in number_list: # Recorre cada número en la lista
    if number == 1: # Verifica si el número es 1
        suffix = 'st' # Asigna el sufijo 'st' para el número 1
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f"{number}{suffix}") # Imprime el número junto con su sufijo correspondiente
    