import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

## invoke the model
llm =ChatGroq( model ="openai/gpt-oss-120b",temperature=0,max_tokens=1024)

## Prompt Template
prompt = PromptTemplate.from_template(
  "Give me the brief information about this sport personality:{name}"
)

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"name":"Sachin Tendulkar"})
print(result)

