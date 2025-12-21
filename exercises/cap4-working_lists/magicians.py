"""muestras de una iteracion usando un bucle for para recorrer una lista de elementos
aparecen en forma de lista vertical mostrando todos los elementos."""

magicians = ['alice', 'david', 'carolina']

for magician in magicians: # keywored for que inicia el bucle, variable magician que toma el valor de cada elemento en la lista magicians,  in palabra reservada que indica la lista a recorrer , seguido de la lista a recorrer
    print(magician) # imprime el valor actual de la variable magician en cada iteracion del bucle   
    print(magician.title() + ", that was a great trick!") # imprime un mensaje personalizado para cada mago en la lista, usando el metodo title() para capitalizar el nombre del mago
    print("I can't wait to see your next trick, " + magician.title() + ".\n") # imprime otro mensaje personalizado para cada mago, seguido de un salto de linea para separar los mensajes de cada iteracion
print("Thank you, everyone. That was a great magic show!") # imprime un mensaje de agradecimiento despues de que el bucle ha terminado

