alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(
    '''                                           
 _______  _______  _______  _______  _______  _______ 
|\     /||\     /||\     /||\     /||\     /||\     /|
| +---+ || +---+ || +---+ || +---+ || +---+ || +---+ |
| |   | || |   | || |   | || |   | || |   | || |   | |
| |c  | || |a  | || |e  | || |s  | || |a  | || |r  | |
| +---+ || +---+ || +---+ || +---+ || +---+ || +---+ |
|/_____\||/_____\||/_____\||/_____\||/_____\||/_____\|
                                                                                                         
 _______  _______  _______  _______  _______  _______ 
|\     /||\     /||\     /||\     /||\     /||\     /|
| +---+ || +---+ || +---+ || +---+ || +---+ || +---+ |
| |   | || |   | || |   | || |   | || |   | || |   | |
| |c  | || |y  | || |p  | || |h  | || |e  | || |r  | |
| +---+ || +---+ || +---+ || +---+ || +---+ || +---+ |
|/_____\||/_____\||/_____\||/_____\||/_____\||/_____\|
                                                      
    '''
)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def transform_message(direction, input_text, shift_value):
    message = ''
    for letter in input_text:
        
        position = alphabet.index(letter)

        if direction == 'encode':
            new_position = position + shift_value

            if new_position > 25:
                message += alphabet[new_position - 26]
            else:
                message += alphabet[new_position]
        
        elif direction == 'decode':
            new_position = position - shift_value
            message += alphabet[new_position]

    print(message)

transform_message(direction=direction, input_text=text, shift_value=shift)

