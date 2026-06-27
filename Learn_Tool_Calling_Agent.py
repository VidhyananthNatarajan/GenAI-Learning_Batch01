import os
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv

##from langchain_openai import Chatopenai

load_dotenv()

@tool
def multiply(a:float,b:float)->float:
    """ This tool has been created for Product of 2 numbers."""
    return a*b

model = ChatGroq(model = "llama-3.3-70b-versatile",temperature =0)

tools =[multiply]

agent = create_agent(model=model,
                          tools=tools,
                          system_prompt="""You are helpful Math Assistant. Provide me the result of the calculations.""")

input_query ="Give me the product for 67.8*56.78?"

responses = agent.invoke ({
 
      "messages":[
                  {
                    "role":"user",
                    "content":input_query   
                  }
                ]       
}

)

# print the response

print(responses["messages"][-1].content)





