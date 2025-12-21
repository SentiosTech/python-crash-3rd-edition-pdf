# Lista de 5 lugares en el mundo
places = ["París, Francia", 
          "Tokio, Japón", 
          "Nueva York, Estados Unidos", 
          "Roma, Italia", 
          "Sídney, Australia"]

print("Lista original:", places)

print("\nOrdenar temporalmente la lista sin modificar la original:", sorted(places))

print("\nLista original después de sorted():", places)

print("\nOrdenar temporalmente la lista en orden inverso sin modificar la original:", sorted(places, reverse=True))

print("\nLista original después de sorted() con reverse:", places)

print("\nInvertir el orden de la lista original:" ,places.reverse())

print("\nOrdenar permanentemente la lista en orden alfabético:", places.sort())
print("\nOrdenar permanentemente la lista en orden inverso:", places.sort(reverse=True))
print("\nLista final después de sort() con reverse:", places)
