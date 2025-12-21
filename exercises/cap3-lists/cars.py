"""muesta usando una funcion interna el ordenamiento alfabetico de la lista,
el cambio se hace permanente, al igual se puede hacer de manera inversa usando
reverse=True"""

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("lista original", cars)
cars.sort()
print('lista ordenada',cars)

cars.sort(reverse=True)
print('lista ordena inversa',cars)

"""ejemplo de una lista ordena temporalmente que crea una nueva lista y que no afecta a la lista orginal"""


print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

"""funcion reverse() que invierte el orden de la lista de manera permanente, que no ordena no la lista alfabeticamente, solo invierte el orden actual de los elementos"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

"""funcion len() que muestra la cantidad de elementos en una lista"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

