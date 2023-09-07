stringToManipulate = '''Du Gamla, Du Fria, Du Fjällhöga Nord
Du Tysta, Du Glädjerika Sköna
Jag Hälsar Dig Vänaste Land Uppå Jord
Din Sol, Din Himmel, Dina Ängder Gröna	
Din Sol, Din Himmel, Dina Ängder Gröna
Du Tronar På Minnen Från Fornstora Dar
Då Ärat Ditt Namn Flög Över Jorden
Jag Vet Att Du Är Och du blir Vad Du Var
Ja, Jag Vill Leva, Jag Vill Dö I Norden
Ja, Jag Vill Leva, Jag Vill Dö I Norden
'''

# Ersätter alla kommatecken med utropstecken!
stringToManipulate = stringToManipulate.replace(",", "!")
stringToManipulate = stringToManipulate.capitalize()
stringToManipulate = stringToManipulate.splitlines()
stringToManipulate = " 卐 ".join(stringToManipulate)
stringToManipulate = stringToManipulate.replace(' 卐 ', ' 卐 \n')
stringToManipulate = stringToManipulate[4:]
print(stringToManipulate)
