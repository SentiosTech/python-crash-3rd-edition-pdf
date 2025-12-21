"""
se muestra un ejemplo donde se realiza un reemplazo, actualizacion o cambio de uno
de los elementos por uno nuevo donde se utiliza el indice como ubicacion de la lista
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

print("lista original",motorcycles)

motorcycles[0] = 'ducati'
print("actualizacion del primer elemento",motorcycles)

"""
ejemplo de agregar un elemento nuevo a la lista con una built in fuction que su accionar
lo hace al final de la lista como distintivo sin afectar los demas elementos
"""

motorcycles.append('ducati')
print("ultimo elemento agregado",motorcycles)

"""
muestra de como crear lista vacia y agregacion de elementos
"""

motors = []

motors.append('honda')
motors.append('yamaha')
motors.append('suzuki')

print("lista vacia,agregando consecutivamente elementos",motors)


"""
ejemplo de como borrar un elemento con indice especifico de la lista,declaracion del
"""

del motors[0]
print(motors)

"""ejemplo de como eliminar el ultimo elemento de la lista y con la habilidad de usar
ese elemento borrado despues de removerlo de la lista, un uso es saber que es el ultimo
elemento adquirido o comprado
"""

popped_motorciclyes = motors.pop()

print(f"la ultima moto tenida fue {popped_motorciclyes.title()}")


"""tambien se puede usar el metodo pop con indice, para decidir cual forma de borrar es
si al eliminar el elemento no se usa mas o se usa"""


"""ejemplo de eliminar elementos por medio el valor del elemento, usando el metodo remove"""

motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']

print(motorcycle)

motorcycle.remove('ducati')
print(motorcycle)

motorscy = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorscy)

too_expensive = 'ducati'

motorscy.remove(too_expensive)

print(motorscy)

print(f"\n una {too_expensive.title} es muy cara para mi")

"""este metodo solo elemina la primera ocurrencia del valor especifico, si hay mas valores
se necesita un bucle for
"""