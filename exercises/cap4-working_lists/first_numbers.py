"""funcion range() sirve para imprimir una secuencia de numeros, una manera sencilla de hacerlo es con un ciclo for
con dos parametros, el primero es el numero inicial y el segundo es el numero final -1
si se usa un solo parametro, el ciclo for empieza en 0 y termina en el numero final -1"""

for value in range(1,5):
    print(value)
# This code prints the first four natural numbers: 1, 2, 3, and 4.
# The range function generates numbers starting from 1 up to, but not including, 5.
# Output:
# 1
# 2
# 3
# 4
# You can change the range parameters to print different sequences of numbers.
# For example, to print the first ten natural numbers, you can use:
"""se puede crear una lista de numeros usando la funcion list() y la funcion range()"""
numbers = list(range(1, 11))
print(numbers)