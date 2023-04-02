'''
Random email generator

1. Generates a random string of x length
2. Append it to random domain name
3. Append it to an array (if it doesn't already exist)

'''

# Import the random module
import random

# Set which characters you want to be in the name part of the email address
valid_characters = 'abcdefghijklmnopqrstuvwyxz1234567890'

# Set the length of the email name field
# For our purposes, between 4 and 15 characters
email_name_length = 10

# Set the amount of email addressses you want to generate
email_address_count = 10
# Instantiate the address list array
email_address_list = []

for i in range(email_address_count):
    # Instantiate (first run) the email name variable. Reset it after each loop
    email_name = ''
    
    # Compile a random set of characters for the email name field
    # For loop will execute as many times as the email_name_length variable is set to
    for i in range(email_name_length):
        # Chooses a random character from the valid_characters variable
        position = random.randint(0, len(valid_characters) - 1)
        # Appends it to the email name
        email_name = email_name + valid_characters[position]

    # Performs a check to see if the first character is a number, and if so replaces it with a letter
    if email_name[0].isnumeric():
        # Chooses a random character from the valid_characters variable, less 10 therefore ensuring it cannot be a number
        position = random.randint(0, len(valid_characters) - 10)
        # Appends it to the email name
        email_name = valid_characters[position] + email_name
        # Removes the last character from the string, ensuring the string is 10 characters in length
        email_name = email_name[:-1]

    # Generate a list of server addresses for the email address
    email_servers=['@gmail', '@yahoo', '@hotmail']
    # Picks a random position within the array
    server_position = random.randint(0, len(email_servers) - 1)

    # Generate a list of top level domain addresses for the email address
    email_top_level_domain=['.com','.gov', '.net', '.org']
    # Picks a random position within the array
    top_level_domain_position = random.randint(0, len(email_top_level_domain) - 1)

    # Combines the name, server and top level domain to create an email address
    email_address = email_name + email_servers[server_position] + email_top_level_domain[top_level_domain_position]

    # Print the email address
    email_address_list.append(email_address)

print('===============================================')
print(f'List of {email_address_count} generated emails')
print('===============================================')
for i in email_address_list:
    print(i)

