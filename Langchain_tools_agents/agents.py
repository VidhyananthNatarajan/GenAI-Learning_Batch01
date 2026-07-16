from langchain.agents import create_agent 
from llm import llm

from tools.web_tool import web_search
from tools.sql_tool import sql_tools
from tools.wiki_tool import wiki_search
from tools.python_tool import python_tool

tools=[web_search,wiki_search,python_tool]

tools.extend(sql_tools)

system_prompt ="""
You are an helpful AI Assistant.

Tool Selection Rules:
-For Current happenings, events or recent trends, use web search tool
-Also provide the website link where the information was reterived.
-For employee related question, use sql tools.
-For Calculation,data analysis, Programming on Python,code execution, use python tools.
-For historical search,Biography, details on Persons, celebrities, Sports person use Wikipedia tools

Always choose the correct tool and validate before answering.
"""
agent = create_agent(
    model =llm,
    tools=tools,
    system_prompt =system_prompt
)
