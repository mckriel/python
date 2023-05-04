PLACEHOLDER = '[name]'
PATH_NAMES = './Input/invited_names.txt'
PATH_LETTER = './Input/starting_letter.txt'
PATH_FINAL_LETTERS = './Output/'


def retrieve_names(file_path):
    with open(file_path) as names_file:
        names_list = names_file.readlines()
    formatted_names = []
    for name in names_list:
        formatted_names.append(name.strip())
    return formatted_names


def retrieve_template(file_path):
    with open(file_path) as file:
        letter = file.read()
    return letter


def write_letters(names_list, letter_template):
    for name in names_list:
        letter = letter_template.replace(PLACEHOLDER, name)
        with open(f'{PATH_FINAL_LETTERS}letter_{name}.txt', 'w') as final_letter:
            final_letter.write(letter)


names = retrieve_names(PATH_NAMES)
template = retrieve_template(PATH_LETTER)

write_letters(names, template)
