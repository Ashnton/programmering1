# Ask user to input a string
user_input = input("Skriv in en valfri sträng: ")

# Define a function to count vowels in the string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Call the function and print the result
print("Antal vokaler i strängen är:", count_vowels(user_input))
