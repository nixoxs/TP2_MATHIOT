import random

def rigged_coin():
    if random.random() < 2/3:
        return "Pile !"
    else:
        return "Face !"

resultat = rigged_coin()
print(resultat)
