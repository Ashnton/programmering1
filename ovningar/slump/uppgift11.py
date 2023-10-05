import random

def testet():
    r = 0
    for i in range(8):
        r += int(random.random() > 0.75)

    return r >= 4
    
antal_lyckade_gånger = 0
i = 0

while (i < 1_000_000):
    i += 1
    antal_lyckade_gånger += int(testet())

print(antal_lyckade_gånger/i)

