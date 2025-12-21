print("Calculando la suma de los números del 1 al 1.000.000...\n")

print("Creando la lista usando una comprensión de listas:")
a_million_list = [number for number in range(1, 1000001)]

print("numero mínimo:", min(a_million_list))
print("numero máximo:", max(a_million_list))

print("\nCreando la lista usando la función list() y range():")
a_million_list = list(range(1, 1000001))

print(f"numero mínimo: {min(a_million_list)}")
print(f"numero máximo: {max(a_million_list)}")

print(f"La suma de los números del 1 al 1.000.000 es: {sum(a_million_list)}")