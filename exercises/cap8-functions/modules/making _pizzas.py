#importar modulo

#se puede crear un alias para la funcion llamada por si hay conflicto con una anterior con el mismo nombre
# from module_name import function_name as fn
from pizza import make_pizza as mp
# si se quiere importar todas la funciones del modulo
# from pizza import *
#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#import pizza
#pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# para importar la funcion primero se pone el nombre del modulo seguido de la funcion separada por un punto
# module_name.function_name()
# para importar funciones especificos: from module_name import function_name
