# Definierar variabler
temp_far = temp_cels = 0

# Ber om användarens input
temp_far = input("Ange temperatur i Fahrenheit: ")

# Omvandlar fahrenheit till celsius
temp_cels = float(temp_far)/1.8 - 32/1.8

# Visar det omvandlade talet på skärmen
print(str(temp_cels) + " grader C")