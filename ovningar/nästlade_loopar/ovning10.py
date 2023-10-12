sum = 0
x = 1
y = 1
z = 1

for x in range(100):
    for y in range(50):
        for z in range(15):
            if ((2*x + 3*y + 7*z) == 102):
                print(x, y, z)