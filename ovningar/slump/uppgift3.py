import random
lista = ["vinst", "vinst", "nit"]
resultat = []

snurr = int(input("Hur många gånger vill du snurra?"))

for n in range (0, snurr):
    resultat.append(random.choice(lista))

print("Antal vinster är:", resultat.count("vinst"), "Andelen vinster är:", resultat.count("vinst")/snurr)
