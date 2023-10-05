# Kvadrattal
kvadrattal = []
bas = 0

while (bas < 100):
    kvadrattal.append(bas**2)
    bas+=1

print(kvadrattal)

# Kubiktal
kubiktal = []
bas = 0
while (bas < (10000**(1/3))):
    kubiktal.append(bas**3)
    bas+=1

print(kubiktal)

# Vilka kvadrattal är också kubiktal?
matchande_tal = set(kvadrattal).intersection(kubiktal)
print(matchande_tal)