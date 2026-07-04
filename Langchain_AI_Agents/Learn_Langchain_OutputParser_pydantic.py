import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel,Field

load_dotenv()

## define the basemodel

class Player(BaseModel):
      name:str = Field(description="Name of the Player")
      age:int = Field(description="Age of the player")
      TotalRuns:int =Field(description="Total runs scored")


## invoke the model
llm =ChatGroq( model ="openai/gpt-oss-120b",temperature=0,max_tokens=1024)

pydantic_parser = PydanticOutputParser(pydantic_object=Player)

## Prompt Template
prompt = PromptTemplate.from_template(
  """Give me the brief information about this sport personality:{name}.I want to get his name,age & total runs scored \n{format_instructions}""",
  partial_variables={"format_instructions":pydantic_parser.get_format_instructions()}
)

chain = prompt | llm | pydantic_parser 
result = chain.invoke({"name":"Sachin Tendulkar"})
print(result)

