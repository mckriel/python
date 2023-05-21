import os
import config
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY


def prompt_query(product):
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=['product'],
        template='What is a good name for a company that makes {product}?',
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    print(chain.run(product))


def main():
    keep_running = True
    while keep_running:
        product_description = input('Input your product: s')
        prompt_query(product_description)


if __name__ == "__main__":
    main()
