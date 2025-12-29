"""ejemplo de la funcion input() que solicita al usuario que ingrese un mensaje"""

active =True  # variable de control para el bucle while identificando si el programa está activo usando flag
while active:  # bucle while que continúa mientras el programa esté activo
    message = input("Tell me something, and I will repeat it back to you: ")

    if message == 'quit':  # condición para verificar si el usuario quiere salir del programa
        active = False  # cambia la variable de control para salir del bucle
    else:
        print(message)
print("¡Fín del programa!")  # mensaje final cuando el programa termina
