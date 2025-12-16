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