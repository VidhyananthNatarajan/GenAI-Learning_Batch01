import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

## invoke the model
llm =ChatGroq( model ="openai/gpt-oss-120b",temperature=0,max_tokens=1024)

# Embedding Model

embeddings =HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5",encode_kwargs={"normalize_embeddings":True})

response = llm.invoke("Say Hello to AI Support Assistant and Ask How was the day?")

print(response.content)


