list4 = [6, 1, 3, 4, 2, 10, 8, 9, 7, 5]

n = len(list4)
for i in range(n):
    swapped = False
    
    for j in range(0, n-i-1):
        if (list4[j] > list4[j+1]):
            tal1 = list4[j]
            tal2 = list4[j+1]
            list4[j] = tal2
            list4[j+1] = tal1
            
            swapped = True
    
    if (swapped == False):
            break

print(list4)