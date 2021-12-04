import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# inputs taken from the user

num_let = int(input("How many letters would you like in your password?\n"))
num_sym = int(input("How many symbols would you like in your password?\n"))
num_num = int(input("How many numbers would you like in your password?\n"))

#easy version
password = "" #starts as an empty string

for char in  range(1, num_let + 1):
    random_char = random.choice(letters)
    password += random_char

for sym in  range(1, num_sym + 1):
    random_sym = random.choice(symbols)
    password += random_sym
    
for num in  range(1, num_num + 1):
    random_num = random.choice(numbers)
    password += random_num

print(password)
    
    
