x_coordinate = float(input("Vad är din x-koordinat?"))
y_coordinate = float(input("Vad är din y-koordinat?"))

if (x_coordinate > 0 and y_coordinate > 0):
    print("Kvadrant 1")

if (x_coordinate < 0 and y_coordinate > 0):
    print("Kvadrant 2")
    
if (x_coordinate < 0 and y_coordinate < 0):
    print("Kvadrant 3")

if (x_coordinate > 0 and y_coordinate < 0):
    print("Kvadrant 4")
