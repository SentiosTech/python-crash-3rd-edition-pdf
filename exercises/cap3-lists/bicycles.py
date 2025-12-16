"""
esto es una representacion y estructura de una lista, que se encuentra dentro de una
varible o el valor de la variable, conjunto de elementos que se cuentan como uno solo
pueden ser de cualquier tipo permitido por el lenguaje, usalmente usado para plurales
coleccion de elementos de un orden particular
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles) # se imprime tal cual aparece en la variable


"""
para acceder a los elementos de las lista, se realiza mediante indices, que tiene la
peculiaridad que el punto de partida es el numero cero (0), en vez del uno, debido
su implementacion de bajo nivel computacional, ejemplo varible signo de lista dentro
del mismo el indice del elemento
"""

print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

"""
este lenguaje tiene una sintaxis especifica para saber el ultimo elemento de la lista
tiene que usar index -1, aplicando esto a la inversa, penultimo[-2],antepenultimo[-3]
"""

print(bicycles[-1])


message = f"mi primera bici fue una {bicycles[0].upper()}"

print(message)