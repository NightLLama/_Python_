motocicletas = ["honda", "yamaha", "suzuki"]
print(motocicletas)

motocicletas[0] = "duque"
print(motocicletas)

motocicletas.append("ducati")
print(motocicletas)

autos = []
autos.append("fiat")
autos.append("ford")
autos.append("chevrolet")
autos.append("hyundai")
print(autos)

# el uso de insert
autos.insert(1, "nissan")
print(autos)

# eliminar un elemento de la lista
del autos[2]
print(autos)

print(motocicletas)
pop_motocicletas = motocicletas.pop()
print(motocicletas)
print(pop_motocicletas)
print("la ultima motocicleta que tuve fue una " + pop_motocicletas)
print("la primera motocicleta que tuve fue una " + motocicletas.pop(0))
print(motocicletas)

# cuando no sabemos el índice del valor que queremos eliminar podemos usar remove
motocicletas.remove("yamaha")
print(motocicletas)
