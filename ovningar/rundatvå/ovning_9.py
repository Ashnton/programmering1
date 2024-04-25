import math

# while True:
#     heltal = int(input("Skriv in ett heltal:"))

#     if heltal > 20:
#         print(heltal**0.5)
#     else:
#         print(heltal**2)
        
while True:
    heltal = int(input("Skriv in ett heltal:"))

    if heltal > 20:
        print(math.sqrt(heltal))
    else:
        print(math.pow(heltal, 2))
