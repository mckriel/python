import turtle
import pandas

PATH_STATE_CSV = '50_states.csv'
PATH_STATE_MAP = 'blank_states_img.gif'
FONT = ("Verdana", 10, "normal")

screen = turtle.Screen()
screen.title('USA State Guessing Game')
image = PATH_STATE_MAP
screen.addshape(image)
turtle.shape(image)

correctly_guessed_states = []


def initialize_state_list():
    df = pandas.read_csv(PATH_STATE_CSV)
    return df.values.tolist()


def check_for_state(state_name, state_list):
    for state in state_list:
        if state_name == state[0]:
            write_state_on_map(state_name, int(state[1]), int(state[2]))
            correctly_guessed_states.append(state)
            return True


def write_state_on_map(state_name, x, y):
    write_text = turtle.Turtle()
    write_text.hideturtle()
    write_text.penup()
    write_text.goto(x, y)
    write_text.write(state_name, font=FONT)


def export_missing_states(guessed_states):
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv('missed-states.csv')


def play():
    continue_game = True
    correct_guess_count = 0
    while continue_game:
        state_guess = screen.textinput(title=f'{correct_guess_count}/50 states guessed',
                                       prompt='Input a state name:').title()
        if state_guess == 'Exit':
            export_missing_states(correctly_guessed_states)
            break
        if check_for_state(state_guess, all_states):
            correct_guess_count += 1


all_states = initialize_state_list()
play()
