from langchain import OpenAI, ConversationChain
import config
import os

os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY


def main():
    llm = OpenAI(temperature=0)
    conversation = ConversationChain(llm=llm, verbose=True)

    keep_running = True
    while keep_running:
        input_string = input('Enter prompt: ')
        output = conversation.predict(input=input_string)
        print(output)


if __name__ == "__main__":
    main()
