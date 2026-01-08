class Dog:# la clase es un model para crear objetos, cuando se crea desde cero no se pone parentesis y siempre se usa tipo title para los nombres de las clases
    # dentro del las clases las funciones cambian de nombre a metodos
    """A simple attempt to model a dog."""
    def __init__(self, name, age): # es una convencion de nombreque se usa para referirse al objeto actual dentro de la clase, creando o usando dentro de la clase
        """Initialize a dog object, name and age attributes."""
        #atributos
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog roll over in response to a command."""
        print(f"{self.name} is now roll over.")


# crear instancia de la clase/objeto
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print("-"*20)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# Clase Dog: molde para crear perros (objetos/instancias)
# __init__ define atributos de cada perro (name, age)
# self apunta al objeto actual que estamos creando o usando
# Métodos sit() y roll_over() usan self para actuar sobre ese perro
# my_dog = Dog('Willie', 6) crea una instancia concreta
# Se puede acceder a atributos con my_dog.name o my_dog.age
# Se puede llamar a métodos con my_dog.sit() o my_dog.roll_over()
