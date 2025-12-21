"""ejemplo de tuplas, son inmutables y se usan para agrupar datos relacionados sin necesidad de modificarlos,
como las dimensiones de un objeto."""

dimensions = (200, 50)
print("mostrar individualmente las dimensiones:")
print(f"indice 0: {dimensions[0]}")
print(f"indice 1: {dimensions[1]}")

"""ejemplo de una tupla con un solo valor, se debe agregar una coma al final para que Python lo reconozca como una tupla."""
# my_t = (3,)

""" no se puede modificar una tupla, pero se puede reasignar la variable a una nueva tupla."""
print("\nDimensiones originales:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nDimensiones modificadas:")
for dimension in dimensions:
    print(dimension)