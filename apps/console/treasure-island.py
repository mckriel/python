'''
Create a simple treasure map game.
The player is given dialogue to read and choices to make.
  
'''

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('')
decision_1 = input('You arrive at a crossroad. Which direction will you go? type Left or Right \n').lower()
if decision_1 == 'left':
    decision_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if decision_2 == 'swim':
        decision_3 = input('What a Chad, you arrive barely wet, unharmed, and not tired at all. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n').lower()
        if decision_3 == "red":
            print("It's a room full of stale Doritos. Game Over.")
        elif decision_3 == "yellow":
            print("You found the treasure! You Win!")
        elif decision_3 == "blue":
            print("It's a room filled with your exes. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif decision_2 == 'wait':
        print('A boat arrives, you board only to discover its filled with angry feminists. Game over.')
    else:
        print('You are not great at reading instrucitons. Start again.')
elif decision_1 == 'right':
    print('You trip, break your ankle. Game over.')
else:
    print('You are not great at reading instrucitons. Start again.')