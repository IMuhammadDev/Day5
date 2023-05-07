import random

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

all_sum = nr_numbers + nr_symbols + nr_letters
new_ar = []
strings = []
nums = []
sym = []

for num in range(1, nr_numbers + 1):
    run = random.randint(0, len(numbers) - 1)
    nums.append(numbers[run])

for stri in range(1, nr_letters + 1):
    run = random.randint(0, len(letters) - 1)
    strings.append(letters[run])

for s in range(1, nr_symbols + 1):
    run = random.randint(0, len(symbols) - 1)
    sym.append(symbols[run])

sum_off_all = strings + sym + nums
print(sum_off_all)
point = len(sum_off_all) - 1
for i in range(0, len(sum_off_all)):
    new_run = random.randint(0, point )
    new_ar.append(sum_off_all[new_run])
    sum_off_all.pop(new_run)
    point = point - 1

print(new_ar)
