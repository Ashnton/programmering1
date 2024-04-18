def jämför_tre_tal():
    tal1 = float(input("Skriv ett tal:"))
    tal2 = float(input("Skriv ett tal:"))
    tal3 = float(input("Skriv ett tal:"))
    
    lista = [tal1, tal2, tal3]
    lista.sort()
    
    print(lista[-1])
    
jämför_tre_tal()