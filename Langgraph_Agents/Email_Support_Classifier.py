import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage,HumanMessage,AIMessage,SystemMessage

from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import tools_condition,ToolNode
from langgraph.graph.message import add_messages
from typing import Annotated,TypedDict,Literal

load_dotenv()

# Define the tools
@tool
def get_billing_information() ->str:
    """ Get information about billing and refund requests"""
    
    return ("Billing Information: Refund requests are reviewed by the billing department. Customer will receive the update in 3-5 business days.") 

@tool
def get_technical_information() ->str:
    """ Get the basic troubleshooting information"""
   
    return ("Technical Troubleshooting: Ask the user to restart the system/application and check for updates.") 

tools =[get_billing_information,get_technical_information]

# Initalize the LLM
llm = ChatGroq(model ="openai/gpt-oss-120b",temperature=0,api_key=os.getenv("GROQ_API_KEY"))

# Define State Schema

class EmailState(TypedDict):
    email_content :str
    category:str
    final_response:str


# Classification node

def classify_node(state:EmailState) ->dict :

    prompt = f"""
                  Classify the customer email content EXACTLY into one of these categories:
                  -Billing
                  -Technical
                  -General

              Email: {state['email_content']}  
              Return ONLY the category name.  
"""
    response = llm.invoke([

                   SystemMessage(content="You're an email classification assistant."),
                   HumanMessage(content=prompt)
                          ]
                        )
    category =response.content.strip()
    return{"category":category}

  # Billing node

def billing_node(state:EmailState) ->dict :

    response = llm.invoke([

                   SystemMessage(content="You're an billing support assistant.Provide a concise and professional response by following responsibleAI practices."),
                   HumanMessage(content=f"CustomerEmail:\n  {state['email_content']}\n. Provide a billing related response.")
                          ]
                        )
    return {"final_response":response.content}


def technical_node(state:EmailState) ->dict :

    response = llm.invoke([

                   SystemMessage(content="You're an technical support assistant.Provide a concise and professional response by following responsibleAI practices."),
                   HumanMessage(content=f"CustomerEmail:\n  {state['email_content']}\n. Provide a technical related response.")
                          ]
                        )
    return {"final_response":response.content}


def general_node(state:EmailState) ->dict :

    return {"final_response":("Thank you for contacting us. Our Customer center representative will call back.")}


## Router Function

def route_email(state:EmailState) -> Literal["billing","technical","general"]:
    category = state["category"].lower()
    if "billing" in category:
        return "billing"
    elif "technical" in category:
        return "technical"
    else:
        return "general"

# Building the Langgraph

builder= StateGraph(EmailState) 
builder.add_node("classify",classify_node)
builder.add_node("billing",billing_node)
builder.add_node("technical",technical_node)
builder.add_node("general",general_node)  
builder.add_node("tools",ToolNode(tools))  

# Building the edges

builder.add_edge(START,"classify")
builder.add_conditional_edges("classify",route_email,{
                                                      "billing":"billing",
                                                      "technical":"technical",
                                                      "general":"general"
                                                      })
builder.add_edge("billing",END)
builder.add_edge("technical",END)
builder.add_edge("general",END)

graph = builder.compile()

test_email={
          "email_content":("I want to know about a product and wanted to give general information about the product.")
}

result = graph.invoke(test_email)

print(f"Category Identified:{result['category']}")
print(f"Final response:{result['final_response']}")
    

