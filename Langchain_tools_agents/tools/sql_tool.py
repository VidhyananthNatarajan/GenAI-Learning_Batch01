from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

from llm import llm

db = SQLDatabase.from_uri("sqlite:///db/employee.db")

toolkit = SQLDatabaseToolkit(db=db,llm=llm)

sql_tools = toolkit.get_tools()