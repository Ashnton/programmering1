# Skapa en tom lista för att lagra uppgifter
todo_list = []

# Skapa en while-loop som fortsätter tills användaren väljer att avsluta programmet
while True:
    # Visa menyn för användaren
    print("Välkommen till att-göra-listan!")
    print("1. Lägg till en ny uppgift")
    print("2. Ta bort en uppgift")
    print("3. Visa hela to-do-listan")
    print("4. Avsluta programmet")

    # Be användaren att välja ett alternativ
    choice = input("Välj ett alternativ: ")

    # Om användaren väljer alternativ 1, be om en ny uppgift och lägg till den i listan
    if choice == "1":
        new_task = input("Skriv in en ny uppgift: ")
        todo_list.append(new_task)
        print("Uppgiften har lagts till i listan.")

    # Om användaren väljer alternativ 2, be om indexet för uppgiften som ska tas bort och ta bort den från listan
    elif choice == "2":
        index = int(input("Skriv in indexet för uppgiften som ska tas bort: "))
        if index < len(todo_list):
            del todo_list[index]
            print("Uppgiften har tagits bort från listan.")
        else:
            print("Indexet är ogiltigt.")

    # Om användaren väljer alternativ 3, visa hela to-do-listan
    elif choice == "3":
        print("Hela to-do-listan:")
        for i, task in enumerate(todo_list):
            print(f"{i}. {task}")

    # Om användaren väljer alternativ 4, avsluta programmet
    elif choice == "4":
        print("Tack för att du använde att-göra-listan!")
        break

    # Om användaren väljer ett ogiltigt alternativ, visa ett felmeddelande
    else:
        print("Ogiltigt val. Försök igen.")
