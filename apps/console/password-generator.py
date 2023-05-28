'''
Random password generator
'''

# Import random class
import random

# Create arrays for letters, numbers & symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('========================================')
print("Welcome to Matthew's Password Generator!")
print('========================================')

# Get the inputs from the user for number of letters, numbers & symbols
num_letters = int(input('How many letters would you like in your password? \n'))
num_numbers = int(input('How many numbers would you like in your password? \n'))
num_symbols = int(input('How many symbols would you like in your password? \n'))

# Instantiate the password list
password_list = []

# Add the letters to the array
for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))

# Add the numbers to the array
for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

# Add the symbols to the array
for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))

# Print the array before the shuffle
print(password_list)
# Shuffle the array
random.shuffle(password_list)
# Print the newly shuffled array
print(password_list)

# Create the password string by iterating over the array
password = ''
for char in password_list:
    password += char

# Print the final password
print(f'Your password is {password}')