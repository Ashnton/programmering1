def calculateTax(salary):
    if (salary < 20000):
        return 0.8
    elif (salary < 30000):
        return 0.75
    elif (salary >= 30000):
        return 0.7
    else:
        return False
    
salary = int(input("Vad är din lön?"))
tax = calculateTax(salary)

print("Du betalar " + str(salary*(1-tax)) + " kr i skatt")
print("Din lön efter skatt är " + str(salary*tax) + " kr")