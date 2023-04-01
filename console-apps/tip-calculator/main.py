'''
Creating a simple tip calculator that:

1. Takes in the total bill amount
2. Requests the tip percentage
3. The amount of people to split the bill with

'''

print('=================================')
print('= Welcome to the tip calculator =')
print('=================================')

# Get some inputs
bill = float(input('Please enter the bill amount: '))
tip = int(input('Please input the tip percentage: '))
people = int(input('Please input the amount of people: '))

# Calculate the tip amount
tip_amount = bill * (tip / 100)
# Calculate what each person should pay
total_each = (bill + tip_amount) / people

# Print out the final result, always having two decimal places.
print(f'Each person should pay: {round(total_each, 2):.2f}')