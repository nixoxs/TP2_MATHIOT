x = float(input("Entrez un nombre : "))

dans_i = (2 <= x < 3) or (0 <= x <= 1) or (-10 <= x <= -2)

if dans_i:
    print(f"{x} appartient à I")
else:
    print(f"{x} n'appartient pas à I")
