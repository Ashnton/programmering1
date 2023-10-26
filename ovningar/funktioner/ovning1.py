def turn_clockwise(direction):
    directions = ["N", "E", "S", "W"]
    return directions[(directions.index(direction)+1)%4]

print(turn_clockwise("S"))