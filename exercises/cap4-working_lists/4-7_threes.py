list_of_3mult = list(range(3, 31, 3))
print("Números múltiplos de 3 entre 3 y 30:")
for number in list_of_3mult:
    print(number)
print("\nUsando una comprensión de listas para crear la misma lista:")
list_of_3mult_comp = [number for number in range(3,31) if number % 3 == 0] # Opción alternativa: range(3, 31, 3)
print(list_of_3mult_comp)