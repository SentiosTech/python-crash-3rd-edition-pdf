"""evitando bucles infinitos"""

x =1 #inicialización de la variable de control
while x <= 5: #condición del ciclo
    print("el valor de x es:",x) #imprime el valor actual de x
    x += 1 #incremento de la variable de control
    # si no se incrementa x, el ciclo nunca terminará, resultando en un bucle infinito y solo muestra 1
print("fin del bucle")