dist_to_trelleborg = float(input("Hur många km är det till Trelleborg? "))
dist_to_moskva = float(input("Hur många km är det till Moskva? "))
dist_to_ramsgate = float(input("Hur många km är det till London? "))
dist_to_hagsätra = float(input("Hur många km är det till Hagsätra? "))
dist_to_düsseldorf = float(input("Hur många km är det till Düsseldorf? "))

table = [["Trelleborg", "Moskva", "London", "Hagsätra", "Düsseldorf"], [dist_to_trelleborg, dist_to_moskva, dist_to_ramsgate, dist_to_hagsätra, dist_to_düsseldorf]]

# Använd zip() för att para ihop städer och avstånd
city_distance_pairs = list(zip(table[0], table[1]))

# Sortera paren baserat på avståndet (andra elementet i paren)
sorted_pairs = sorted(city_distance_pairs, key=lambda pair: pair[1])

# Dela upp paren igen i separata listor för städer och avstånd
sorted_cities = [pair[0] for pair in sorted_pairs]
sorted_distances = [pair[1] for pair in sorted_pairs]

# Uppdatera den ursprungliga tabellen med de sorterade listorna
table[0] = sorted_cities
table[1] = sorted_distances

for row in table:
    print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'.format(*row))
