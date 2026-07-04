import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

## invoke the model
llm =ChatGroq( model ="openai/gpt-oss-120b",temperature=0,max_tokens=1024)

##PromptTemplate
prompt_1=ChatPromptTemplate.from_template(
   "You're an Assistant helping to generate the only one company name for the given product idea.Here is the  product idea:{product_idea}")

prompt_2 =ChatPromptTemplate.from_template(
   "You're an Assistant helping to generate the only one company description from the idea and company name.Here is the product idea:{product_idea} and the company name:{company_name}")

prompt_3=ChatPromptTemplate.from_template(
   "You're an Assistant helping to generate the only one company Objective from the idea,company name & description.Objective should be short and catchy. Here is the product idea:{product_idea} and the company name:{company_name} and the company description:{company_description}")

chain1 =prompt_1|llm|StrOutputParser()
chain2 =(RunnablePassthrough.assign(company_name = chain1)|prompt_2|llm|StrOutputParser())
chain3 =(RunnablePassthrough.assign(company_name = chain1,company_description=chain2)|prompt_3|llm|StrOutputParser())

chain =(RunnablePassthrough.assign(company_name = chain1).assign(company_description = chain2).assign(company_objective = chain3))

result = chain.invoke({"product_idea":"An Online platform where people can register their infromation and share their views on various happenings."})

print(result)