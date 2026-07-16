from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

@tool
def web_search(query:str)->str:
    """
    Search the internet for the current information. 
    
    """
    return search.run(query)