def slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)

def intercept(x1, y1, x2, y2):
    return y1-(slope(x1, y1, x2, y2)*x1)

print(intercept(1, 6, 3, 12))