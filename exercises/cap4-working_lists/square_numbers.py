""" ejemplo de crear una lista con los cuadrados de los números del 1 al 10"""

squares = []  # Crear una lista vacía
for value in range(1, 11):  # Iterar sobre los números del 1 al 10
    square = value ** 2  # Calcular el cuadrado del número
    squares.append(square)  # Agregar el cuadrado a la lista
print(squares)  # Imprimir la lista de cuadrados