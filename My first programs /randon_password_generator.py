import random
from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
for a in range(0,nr_letters):
    password += random.choice(letters)
for a in range(1,nr_symbols):
    password += random.choice(symbols)
for a in range(1,nr_numbers):
    password += random.choice(numbers)
random.shuffle(password)
final_pass = ""
for char in password:
    final_pass += char
print(f"Your password is: {final_pass}")
#or it can also work this way:
# final_pass = "".join(password)
# print(f"Your password is: {final_pass}")






