"""
los f-strings son una manera de formato para order el contenido de las variables
o unan manera de concatenar donde dentro de los parentesis van dentro de corchetes
las variables definidas y afuera de las comilla va la letra f que es su carecteristica
"""

first_name = "ada"
last_name = " lovelace"
full_name = f"{first_name} {last_name}"


print(full_name)
#print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

