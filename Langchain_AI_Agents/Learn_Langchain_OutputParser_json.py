import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

## invoke the model
llm =ChatGroq( model ="openai/gpt-oss-120b",temperature=0,max_tokens=1024)

json_parser = JsonOutputParser()

## Prompt Template
prompt = PromptTemplate.from_template(
  """Give me the brief information about this sport personality:{name}.I want to get his name,age & total runs scored \n{format_instructions}""",
  partial_variables={"format_instructions":json_parser.get_format_instructions()}
)

chain = prompt | llm | json_parser
result = chain.invoke({"name":"Sachin Tendulkar"})
print(result)

