import pandas


def load_alphabet():
    df = pandas.read_csv('nato_phonetic_alphabet.csv')
    return {row.letter: row.code for (index, row) in df.iterrows()}


def produce_nato(df):
    nato_input = input('Enter a word: ').upper()
    nato_output = [df[letter] for letter in nato_input]
    return nato_output


def main():
    run = True
    df = load_alphabet()

    while run:
        print(produce_nato(df))
