import config
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY
os.environ["SERPAPI_API_KEY"] = config.SERPAPI_API_KEY


def main():
    llm = OpenAI(temperature=0)
    tools = load_tools(['serpapi', 'llm-math'], llm=llm)
    agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    # test prompt
    agent.run(
        'What was the high temperature in Cape Town yesterday in celsius? then multiply that number by itself and give me both the temperature and the number multipied by itself rounded to the nearest whole number')


if __name__ == "__main__":
    main()
