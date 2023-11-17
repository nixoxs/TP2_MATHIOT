nombre = int(input("Écrivez un Nombre"))

if nombre > 0:
    signe = "positif"

elif nombre < 0:
    signe = "négatif"

else:
    signe = "zéro"


if nombre % 2 == 0:
    parite ="pair"

else:
    parite = "impair"


if signe == "zero":
    print("Le nombre est", signe, "(et il est", parite, ").")

else:
    print("Le nombre est", signe, "et", parite,".")