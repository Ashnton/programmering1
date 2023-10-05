import random
utfall = ["röd", "gul", "röd", "röd"]

# a)
for i in range (10):
    print(random.choice(utfall))

# b)
resultat = []
for i in range (10):
    resultat.append(random.choice(utfall))
    print(resultat[-1])
    print(resultat.count("röd"))
    print(resultat.count("gul"))