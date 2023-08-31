# Definierar variabler
dollarkurs = 10.90
dollar = sek = 0

dollar = input("Hur många dollar vill du omvandla till SEK?")

# För att omvandla dollar till SEK
sek = int(dollar) * dollarkurs

# Visar resultatet av omvandlingen för användaren
print(str(dollar) + " dollar motsvarar " + str(sek) + " svenska kronor")