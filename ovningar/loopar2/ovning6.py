number = int(input("Skriv in ett tal:"))
if (number > 10 and number % 2 == 0):
    print("Talet är större än tio och jämnt")

if (number > 100 and number % 2 != 0):
    print("Talet är större än hundra och udda")

if (number < 0 and number % 3 == 0):
    print("Talet är negativt och delbart med tre")

if (number < 0 and number % 3 == 0 and number % 2 == 0):
    print("Talet är negativt och delbart med två och tre")

if (number % 2 != 0 and number % 3 != 0):
    print("Talet är varken delbart med två eller tre")