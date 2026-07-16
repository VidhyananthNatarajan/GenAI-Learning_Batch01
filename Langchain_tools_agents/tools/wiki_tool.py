from langchain_core.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper

wiki_search = WikipediaAPIWrapper()

@tool
def wiki_search (query:str)->str:
    """
    Search the given input in Wikipedia.com 
    
    """
    return wiki_search.run(query)