prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = "" # inicialización que almacena el mensaje del usuario antes del bucle
while message.lower() != 'quit': # condición para continuar el bucle
    message = input(prompt) # cuerpo del bucle: solicita al usuario que ingrese un mensaje

    if message.lower() != 'quit': # condicion de comprobacion si el mensaje es diferente de 'quit'
        print(message) # imprime el mensaje ingresado por el usuario
    else:
        print("¡Fín del programa!") # mensaje final cuando el usuario ingresa 'quit'