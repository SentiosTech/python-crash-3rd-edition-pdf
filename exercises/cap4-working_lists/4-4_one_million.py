one_million_numbers_list = []
print("Creando una lista de números del 1 al 1.000.000...\n")

print("usando un bucle for:")
for number in range(1, 1000001):
    one_million_numbers_list.append(number)
print(f"lista creada con {len(one_million_numbers_list)} números.")

print("\nusando comprehensión de listas:")

one_million_number_list = [number for number in range(1, 1000001)]
print(f"lista creada con {len(one_million_number_list)} números.")