input = list(input('Skriv in något valfritt: '))

i = 0
inputString = ""
while i < len(input):
    if (i % 2 == 0):
        inputString += input[i].upper()
    else:
        inputString += input[i].lower()
    i+=1
    
print(inputString)