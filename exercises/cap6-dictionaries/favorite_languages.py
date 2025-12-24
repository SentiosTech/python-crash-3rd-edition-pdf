favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language.title()}.")

print("\n--- All favorite languages ---")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
print("\n--- Names in the dictionary ---")
for name in favorite_languages.keys(): # se puede omitir .keys(), ya que es la misma acción por defecto
    print(name.title())
    
print("\n--- Checking for specific people ---")
friends = ['phil', 'sarah']
for name in favorite_languages.keys(): # recorremos las claves del diccionario
    print(f"Hi {name.title()}.") # saludo genérico
    if name in friends: # si el nombre está en la lista de amigos
        language = favorite_languages[name].title() # obtenemos su lenguaje favorito, y lo capitalizamos
        print(f"\t{name.title()}, I see you love {language}!") # mensaje personalizado para amigos
    if 'erin' not in favorite_languages.keys(): # verificamos si 'erin' no está en las claves del diccionario
        print("Erin, please take our poll!") # invitación a participar en la encuesta
    
print("\n--- Sorted names ---")
for name in sorted(favorite_languages.keys()): # recorremos las claves del diccionario en orden alfabético
    print(f"{name.title()}, thank you for taking the poll.") # mensaje de agradecimiento
    
print("\n--- Show only values ---")

print("\nLanguages mentioned:")
for language in favorite_languages.values(): # recorremos los valores del diccionario   
    print(language.title()) # imprimimos cada lenguaje capitalizado

print("\n--- Using set to show unique values ---")
print("\nLanguages mentioned (unique):") # para evitar duplicados y cuando es una lista grande
for language in set(favorite_languages.values()): # recorremos los valores únicos del diccionario
    print(language.title()) # imprimimos cada lenguaje capitalizado