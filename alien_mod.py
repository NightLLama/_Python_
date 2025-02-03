alien_0 = {"x_position": 0, "y_position": 25, "velocidad": "media"}
print("Posición x original: " + str(alien_0["x_position"]))

# Mueve al alienígena a la derecha
# De acuerdo con la velocidad actual del alienígena, qué tan lejos moverlo

if alien_0["velocidad"] == "lento":
    x_increment = 1
elif alien_0["velocidad"] == "medio":
    x_increment = 2
else:
    # Este alienigena debe ser rápido
    x_increment = 3

# la nueva posición es igual a la posición anterior más el incremento
alien_0["x_position"] = alien_0["x_position"] + x_increment
print("Nueva posición x: " + str(alien_0["x_position"]))
print(alien_0)
del alien_0["x_position"]
print(alien_0)
