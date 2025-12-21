dinner_list = ['blue','red','gold','purple']

print("solo dos pueden ser invitados")

dinner_list.pop()
print("haz sido eliminado",dinner_list[-1])
dinner_list.pop()

print("haz sido eliminado",dinner_list[-1])

print("aun estan invitados", dinner_list[0],dinner_list[1])

del dinner_list
