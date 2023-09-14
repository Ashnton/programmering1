import numpy as np

# Koefficientmatris A
A = np.array([[1, 1],
              [500, 100]])

# Konstantvektor b
b = np.array([65, 19700])

# Använd numpy.linalg.solve för att lösa ekvationssystemet
solution = np.linalg.solve(A, b)

# Lösningen är i form av en array [x, y]
x = round(solution[0])
y = round(solution[1])

print(f'Lösning: {x} 500-lappar, {y} 100-lappar')