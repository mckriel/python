'''
Rock, Paper, Scissors
'''

# Import the random library
import random

# Set the visual variables of Rock, Paper and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Put the images into an array
choice_images = [rock, paper, scissors]

# Instantiate the player choice variable
choice_player = ''

# Keep looping until the player inputs a 0
while choice_player != '0':
    
    # Display messages to the player
    print("What do you choose? Rock, Paper or Scissors?")
    print('1 - Rock')
    print('2 - Paper')
    print('3 - Scissors')
    print('0 - Quit game')

    # Attempt to execute the code, restart the loop if something goes wrong
    # Main purpose is to handle if a letter is input
    try:
        # Get the players input and cast it to an integer
        choice_player = int(input("Input your number: "))
        # Choose a random number between 1 and 3 for the computer player
        choice_computer = random.randint(1,3)

        # If the player chooses 4 or higher, print out a message
        if choice_player >= 4:
            print('You typed an invalid number.')
        # Close the game if the user inputs 0
        elif choice_player == 0:
            print('Closing game. Thank you for playing.')
            break
        # Logic for an accepted input
        else:
            # Print out the choices 
            print('You chose:')
            print(choice_images[choice_player - 1])
            print('Computer chose:')
            print(choice_images[choice_computer - 1])

            # Outcomes where player chooses Rock
            if choice_player == 1 and choice_computer == 1:
                print('DRAW!')
            elif choice_player == 1 and choice_computer == 2:
                print('YOU LOSE!')
            elif choice_player == 1 and choice_computer == 3:
                print('YOU WIN!')

            # Outcomes where player chooses Paper
            elif choice_player == 2 and choice_computer == 1:
                print('YOU WIN!')
            elif choice_player == 2 and choice_computer == 2:
                print('DRAW!')
            elif choice_player == 2 and choice_computer == 3:
                print('YOU LOSE!')

            # Outcomes where player chooses Scissors
            elif choice_player == 3 and choice_computer == 1:
                print('YOU LOSE!')
            elif choice_player == 3 and choice_computer == 2:
                print('YOU WIN!')
            elif choice_player == 3 and choice_computer == 3:
                print('DRAW!')
            
            else:
                print('Incorrect input, try again.')
    except:
        print('Please input numbers only. Try again')
        continue
        

    