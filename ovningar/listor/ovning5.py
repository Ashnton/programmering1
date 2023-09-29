gräns = int(input("Ange valfritt heltal: "))

lista = []
n = 5
a = 1
värde = 14
while (a <= gräns):
    lista.append(n)
    n = n + 3
    a = a + 1
    värde = värde + 12
    
print(lista)
print(värde-12)