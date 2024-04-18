Ämnen = ["matte", "datorteknik", "nätverksteknik"]

# Skriver ut antalet element i listan
print(len(Ämnen))
print(Ämnen)


Ämnen.append("programmering")
print(Ämnen)

Ämnen[1] = "nätverksteknologier"
print(Ämnen)

Ämnen.pop(2)
print(Ämnen)

Ämnen.remove("matte")
print(Ämnen)
 
for i in Ämnen:
    print(i)
    
Ämnen.clear()
print(Ämnen)