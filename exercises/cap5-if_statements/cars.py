"""ejemplo de condicional if usando ciclo for para recorrer una lista de autos
si el auto es 'bmw' imprime en mayusculas, de lo contrario en titulo"""

cars = ['audi', 'bmw', 'subaru', 'toyota']
print("Lista de autos:")
print(cars,"\n")
print("Imprimiendo nombres de autos con condicional if:\n")


for car in cars: #recorre cada auto en la lista cars
    if car == 'bmw': #condicional if para verificar si el auto es 'bmw'
        print(car.upper()) #imprime el auto en mayusculas
    else: #si no es 'bmw'
        print(car.title()) #imprime el auto en formato titulo

print("\nFin del programa.")
