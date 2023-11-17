a = input("définir a :")
b = input("définir b :")
print("Avant l'échange")
print("a:", a, "b:", b)
temp = a
a = b
b = temp
del temp
print("Après l'échange")
print("a:", a, "b:", b)