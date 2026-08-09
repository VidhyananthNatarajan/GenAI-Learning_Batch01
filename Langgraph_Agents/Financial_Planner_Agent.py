import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage,HumanMessage,AIMessage,SystemMessage

from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import tools_condition,ToolNode
from langgraph.graph.message import add_messages
from typing import Annotated,TypedDict


load_dotenv()

# Define the tools
@tool
def get_stock_price(stock:str) ->str:
    """ simulates/fetches the real time stock price for a given stock."""
    prices ={"AAP":"$185.50","GOOGLE":"$150.03","META":"$199.03"}
    return prices.get(stock.upper(), "Stock not found.")

@tool
def calculate_growth(initial:float,final:float) ->str:
    """ Calculate the growth percentage"""
    pct_change =((final-initial)/initial)*100
    return f"{pct_change:.2f}%"

tools =[get_stock_price,calculate_growth]

# Initalize the LLM
llm = ChatGroq(model ="openai/gpt-oss-120b",temperature=0,api_key=os.getenv("GROQ_API_KEY"))
llm_with_tools = llm.bind_tools(tools)

# Define the state schema
class AgentState(TypedDict):
     messages:Annotated[list[BaseMessage],add_messages]

# Create the Agent Node
def agent_node(state: AgentState) -> dict:
     response = llm_with_tools.invoke(state["messages"])  
     return {"messages":[response]}  

#Build ReAct Graph

builder = StateGraph(AgentState)
builder.add_node("agent",agent_node)
builder.add_node("tools",ToolNode(tools))

builder.add_edge(START,"agent")
builder.add_conditional_edges("agent",tools_condition)
builder.add_edge("tools","agent")
builder.add_edge("agent",END)

react_agent = builder.compile()

#message = HumanMessage(content="What is the stock price of META. What would be growth if it moves to 235.07?")
#msg = react_agent.invoke({"messages":message})

#print(msg)

query ="What is the stock price of META. What would be growth if it moves to 235.07?"
inputs ={"messages":[HumanMessage(content=query)]}

for chunk in react_agent.stream(inputs,stream_mode="values"):
    latest_message=  chunk["messages"][-1]
    print(f"\n[{latest_message.type.upper()}]: {latest_message.content}")
    if hasattr(latest_message,"tool_calls") and latest_message.tool_calls:
        print(f"Tool Calls Requested: {latest_message.tool_calls}")
     