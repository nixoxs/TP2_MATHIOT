import random

nombre_random = random.randint(0, 100)

if nombre_random < 50:
    resultat = "Pile !"

else:
    resultat = "Face !"

print(resultat)
