from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
  model ="openai/gpt-oss-120b",  ##openai/gpt-oss-20b,openai/gpt-oss-20b    
  temperature =0,
  api_key=os.getenv("groq_api_key")
)

