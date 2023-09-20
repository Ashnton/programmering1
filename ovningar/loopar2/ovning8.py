price = int(input("Hur mycket är varorna värda?"))
delivery = input("Vill du ha frakt?")
private = input("Är du en privatperson?")

if (private == "Ja" or private == "ja"):
    price = price * 1.25

if (delivery == "Ja" or delivery == "ja"):
    price = price + 59

print(price)