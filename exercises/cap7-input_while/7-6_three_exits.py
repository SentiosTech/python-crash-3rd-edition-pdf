# MOVIE TICKET PRICE CALCULATOR - 3 EXIT METHODS

print("=" * 50)
print("MOVIE TICKET PRICE - THREE EXIT METHODS")
print("=" * 50)

# ============================================
# WHILE LOOP para validar la opción
# ============================================

method = ""

while True: #validacion
# choice of method
    print("Choose an exit method to test:")
    print("1. Conditional test in while statement")
    print("2. Active variable (flag)")
    print("3. Break statement")
    print("Enter 'quit' to end the program.\n")
    
    
    method = input("\nEnter 1, 2, 3 or 'quit':")
    
    print(f"\nDEBUG: method = '{method}'")  # ← Agrega esto
    print(f"DEBUG: type = {type(method)}")  # ← Y esto
    print(f"DEBUG: method in [1,2,3] = {method in [1,2,3]}\n")  # ← Y esto

    if method.lower() == 'quit':
        print("Bye!!")
        print("="*50)
        break
    
    elif method in ['1', '2', '3']:  
        print(f"you selected method {method}")
        print("="*50)
        break

    else:
        print("⚠️ \nPlease enter 1, 2, 3, or 'quit' only.\n")
        continue  # Vuelve al inicio del while



# ============================================
# MÉTODO 1: Conditional test in while statement
# ============================================

if method == '1':
    
    print("\n" + "="*50)
    print("🔹 METHOD 1: while age != 'quit'")
    print("="*50)
    

    age = ""  # inicialización que almacena la edad del usuario antes del bucle

    while age != 'quit':  # condición para continuar el bucle
        age = input("\nAge? (or 'quit'): ")  # cuerpo del bucle: solicita al usuario que ingrese su edad
        
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
            
# ============================================
# MÉTODO 2: Active variable (flag)
# ============================================

elif method == '2':
    print("\n" + "="*50)
    print("🔹 METHOD 2: Active variable (flag)")
    print("="*50)
    
    active = True # control variable to manage the loop
    
    while active: # loop continues while active is true
        age = input("\nAge? (or 'quit'): ")  # solicita al usuario que ingrese su edad
        
        if age.lower() == 'quit': # si el usuario ingresa 'quit'
            active = False  # cambia la variable de control a falso para salir del bucle
            print("Exiting the program...")  # mensaje de salida
            print("Thank you for using the movie ticket price calculator!")  # mensaje final cuando el usuario ingresa 'quit'

        else:
            age = int(age)  # convierte la entrada del usuario a un entero
            
            if age < 3:  # condición para menores de 3 años
                price = 0
            elif 3 <= age <= 12:  # condición para edades entre 3 y 12 años
                price = 10
            else:  # condición para mayores de 12 años
                price = 15
                
            print(f"Your movie ticket price is ${price}.")  # muestra el precio del boleto
    
# ============================================
# MÉTODO 3: Active variable (flag)
# ============================================

elif method == '3':
    
    print("\n" + "="*50)
    print("🔹 METHOD 3: Break statement")
    print("="*50)
    
    while True:
        age = input("\nAge? (or 'quit'): ")
        
        if age.lower() == 'quit':
            print("Thank you for using the movie ticket price calculator!")  # mensaje final cuando el usuario ingresa 'quit'
            break
        
        else:
            age = int(age)  # convierte la entrada del usuario a un entero
            
            if age < 3:  # condición para menores de 3 años
                price = 0
            elif 3 <= age <= 12:  # condición para edades entre 3 y 12 años
                price = 10
            else:  # condición para mayores de 12 años
                price = 15
                
                print(f"Ticket price: ${price}")
                