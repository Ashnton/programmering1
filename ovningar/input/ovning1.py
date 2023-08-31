first_number = int(input("Ange ett heltal: "))
second_number = int(input("Ange ytterligare ett heltal: "))

# För att visa datan i en tabell
table = [["Summa:", "Differans:", "Kvot:", "Produkt:"], [first_number+second_number, first_number-second_number, first_number/second_number, first_number*second_number]]
for row in table:
    print('| {:^10} | {:^10} | {:^10} | {:^10} |'.format(*row))