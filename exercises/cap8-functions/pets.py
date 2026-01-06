def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
    print(f"\ni have a {animal_type}")
    print(f"\n{animal_type}'s name is {pet_name}")

describe_pet('hamster', 'harry')
print("-" * 25)
describe_pet('dog','whillie')
print("-" * 25)
describe_pet(animal_type='parrot', pet_name='john')
# el orden importa en la posicion de argumentos

# valor por defecto
#def describe_pet(animal_type = 'dog'):
"""Display information about a pet."""
#    print(f"\ni have a {animal_type}")
#   print(f"\n{animal_type}'s name is {pet_name}")

#describe_pet(animal_type='hamster')
#argumento explicito
#describe_pet(pet_name='harry', animal_type='hamster')

"""
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
"""