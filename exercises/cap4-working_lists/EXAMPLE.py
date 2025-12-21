lis1 = [1, 3, 5, 7]
lis2 = [2, 4, 6, 8]
print("Usando una comprehension list:")
pair_list = [(x,y) for x in lis1 for y in lis2 if x!=y]
print(pair_list)

print("\n")
print("Otra forma de hacerlo, usando bucles anidados:")
for x in lis1:
    for y in lis2:
        if x != y:
            print((x,y))