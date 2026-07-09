import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("groq_api_key")

COLLECTION_NAME="SOP_doc"
CHROMA_PATH="./chroma_db"
TOP_K=5
LLM_MODEL="llama-3.3-70b-versatile"
EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"