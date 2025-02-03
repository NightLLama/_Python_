cuadrados = []
for valor in range(1, 11):
    cuadrado = valor**2
    cuadrados.append(cuadrado)

print(cuadrados)

cuadrados_mod = []
for valor in range(1, 6):
    cuadrados_mod.append(valor**2)

print(cuadrados_mod)

# 2 funciones importantes, la función min y max
print("el valor max de la lista es:", max(cuadrados_mod))
print("el valor minimo de la lista es:", min(cuadrados_mod))

# también podemos crear listas por compresnsion

cuadrados_mod2 = [valor**2 for valor in range(1, 11)]
print(cuadrados_mod2)
