import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


load_dotenv()

## invoke the model
llm =ChatGroq( model ="openai/gpt-oss-120b",temperature=0,max_tokens=1024)

##Creating the prompt template

prompt =PromptTemplate(
  input_variables=["country"],
  template="""
            You are a helpful AI Assistant. I am located at the {country}.
            Give me 3 line description about this country?

   """
)
chain = prompt|llm
#response = chain.invoke({"country":"India"})

countries=[{"country":"USA"},{"country":"United Kingdom"},{"country":"Australia"}]



#responses = chain.batch(countries)

#for response in responses:
#    print(response.content)

#for response in chain.stream({"country":"India"}):
#    print(response.content)
