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

choice_player = ''

while choice_player != '0':
    print("What do you choose? Rock, Paper or Scissors?")
    print('1 - Rock')
    print('2 - Paper')
    print('3 - Scissors')
    print('0 - Quit game')
    choice_player = int(input("Input your number: "))
    choice_computer = random.randint(1,3)

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