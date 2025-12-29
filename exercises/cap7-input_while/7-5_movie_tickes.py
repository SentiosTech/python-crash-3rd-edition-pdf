prompt = "\nTell me your age, and I will tell you the price of your movie ticket:"
prompt += "\nEnter 'quit' to end the program. "

age = ""  # inicialización que almacena la edad del usuario antes del bucle

while age != 'quit':  # condición para continuar el bucle
    age = input(prompt)  # cuerpo del bucle: solicita al usuario que ingrese su edad
    
    if age.lower() != 'quit':  # condicion de comprobacion si la edad es diferente de 'quit'
        age = int(age)  # convierte la entrada del usuario a un entero
        
        if age < 3:  # condición para menores de 3 años
            price = 0
        elif 3 <= age <= 12:  # condición para edades entre 3 y 12 años
            price = 10
        else:  # condición para mayores de 12 años
            price = 15
            
        print(f"Your movie ticket price is ${price}.")  # muestra el precio del boleto
    else:
        print("Thank you for using the movie ticket price calculator!")  # mensaje final cuando el usuario ingresa 'quit'