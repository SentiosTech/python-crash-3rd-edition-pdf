prompt = "\nTell me a series of pizza toppings or"
prompt += "\nEnter 'quit' to end the program. "

data_input = ""  # inicialización que almacena la entrada del usuario antes del bucle
while data_input.lower() != 'quit':  # condición para continuar el bucle    
    data_input = input(prompt)  # cuerpo del bucle: solicita al usuario que ingrese un topping
    
    if data_input.lower() != 'quit':  # condicion de comprobacion si el topping es diferente de 'quit'
        print(f"I'll add {data_input} to your pizza!")  # confirma el topping ingresado por el usuario
        
    else:
        print("Your pizza is being prepared!")  # mensaje final cuando el usuario ingresa 'quit'