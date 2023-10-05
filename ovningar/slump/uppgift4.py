import random

udda = [1, 3, 5 , 7, 9]
jämna = [2, 4, 6, 8, 10]

# a)
tal = random.choice(udda) + random.choice(jämna)
print(tal)

# b)
# Resultatet blir alltid udda eftersom udda plus jämnt inte kan bli jämnt

# c)
tal = random.choice(udda) * random.choice(jämna)
print(tal)

# d) Udda gånger jämnt blir jämnt