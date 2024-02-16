def addera_tal(lista):
    return lista[-1] + lista[-2]

i = 0
lista = [0, 1]
while i < 10:
    lista.append(addera_tal(lista))
    i+=1
print(lista)