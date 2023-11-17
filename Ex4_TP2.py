base = 4
fromage = 8000.0
eau = 2
ail = 2
pain = 400
Convives = int(input( "Indiquez le nombre de convives :"))
fromage = fromage * Convives / base
eau = eau * Convives / base
ail = ail * Convives / base
pain = pain * Convives / base
print("Pour faire une fondue fribourgeoise pour", Convives, "personne(s), il vous faut :")
print(fromage, "grammes de fromage,", eau, "décilitres d'eau,", ail, "gouses(s) d'ail, et", pain, "grammes de pain.")