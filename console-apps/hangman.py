import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


print('''
 _                                                   
| |__    __ _  _ __    __ _  _ __ ___    __ _  _ __  
| '_ \  / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \ 
| | | || (_| || | | || (_| || | | | | || (_| || | | |
|_| |_| \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_|
                      |___/                          
''')
print('==================')
print('WELCOME TO HANGMAN')
print('==================')

# Set game variables
end_of_game = False
display = []
word_list = ['granite', 'spider', 'godlike', 'genius']
attempts = 6

# Choose a random word from the array
chosen_word = random.choice(word_list)

# Find out the word length
chosen_word_length = len(chosen_word)

# Fill the display array with _ for each letter of the chosen word
for letter in chosen_word:
    display += '_'

# Keep looping until end_of_game becomes True
while not end_of_game:

    # Player inputs a guess
    print(stages[attempts])
    print(f'You have {attempts} attempts left :) \n')
    guess = input('Guess a letter: ').lower()

    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        attempts -= 1

    print(display)

    if '_' not in display:
        print('You win!')
        end_of_game = True
    elif attempts == 0:
        print(stages[attempts])
        print('You lose')
        end_of_game = True

