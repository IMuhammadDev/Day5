import random

# Define the lists of letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get user input for the number of letters, symbols, and numbers they want in their password
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generate a list of all characters to be included in the password
all_chars = letters + symbols + numbers

# Generate separate lists for the letters, symbols, and numbers
strings = random.choices(letters, k=nr_letters)
nums = random.choices(numbers, k=nr_numbers)
sym = random.choices(symbols, k=nr_symbols)

# Combine the separate lists into a single list
password_list = strings + sym + nums

# Shuffle the list using the shuffle() function from the random module
random.shuffle(password_list)

# Convert the list to a string and print it
password = ''.join(password_list)
print(f"Your password is: {password}")
