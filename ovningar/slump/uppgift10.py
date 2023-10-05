import random

input = input("Sten sax påse:").lower()
datorn = ["sten", "sax", "påse"]
datorval = random.choice(datorn)

if (input == datorval):
    print("Oavgjort")
elif (input < datorval):
    print("Datorn vinner")
elif (input > datorval):
    print("Du vinner")