talet = int(input("Skriv ett valfritt positivt heltal:"))
while (talet != 1):
    if (talet % 2 == 0):
        talet = talet/2
    else:
        talet = (talet*3)+1
    
    print(talet)

print(talet)