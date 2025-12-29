"""ejemplo de uso de la funcion break para salir de un bucle while"""

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:  # bucle infinito que continuará hasta que se encuentre una declaración break
    city = input(prompt)  # solicita al usuario que ingrese el nombre de una ciudad
    
    if city.lower() == 'quit':  # condición para verificar si el usuario quiere salir del bucle
        print("¡Fín del programa!")  # mensaje final cuando el usuario termina de ingresar ciudades
        break  # sale del bucle si el usuario ingresa 'quit'
    else:
        print(f"I'd love to go to {city.title()}!")  # responde con un mensaje sobre la ciudad ingresada