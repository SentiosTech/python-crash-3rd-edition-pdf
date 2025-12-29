"""ejemplo de uso de continuar en un ciclo while mostrando solo números impares del 1 al 10"""


current_number = 0 #inicialización de la variable de control
while current_number < 10: #condición del ciclo
    current_number += 1 #incremento de la variable de control
    if current_number % 2 == 0: #verifica si el número es par
        #print("Número par encontrado y omitido..") #imprime el número par encontrado
        continue #salta a la siguiente iteración si el número es par

    print("numero impar es:",current_number) #imprime el número si es impar
