'''
Create a super simple console app that generates a band name
based on your home town and pet name.
'''

# Import the time module to make use of the pause functionality
import time

# Print the welcome message
print('Welcome to the band name generator.')

# Prompt the user for their city and pet name
input_city = input('What city did you grow up in? ')
input_pet = input('What is the name of your pet? ')

# Sleep the program a few times to add some suspense
print('One sec while we generate your band name...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')

# Print the generated band name
print('Your band name is: ' + input_city + ' ' + input_pet)