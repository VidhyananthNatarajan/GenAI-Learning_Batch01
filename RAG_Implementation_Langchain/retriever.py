import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_client =Groq(api_key=os.getenv("groq_api_key"))
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

## Get the Collection details

def get_collection():
    client = chromadb.PersistentClient(path = "./chroma_db")
    collections = client.list_collections()

    return client.get_collection("project_docs")

## reterive the context
def retrieve_context(query,top_k=3):
    collection = get_collection()

    query_embedding = embedding_model.encode(query).tolist()

    results =collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents =results["documents"][0]

    return "\n".join(documents)

## Call the Model -- llama via Groq

def ask_llama(context,query,chat_history=None):
    history_text =""
    if chat_history:
        for msg in chat_history:
            history_text += f"{msg['role']}: {msg['content']} \n"
    prompt  = f"""
        You're an helpful assistant. use context and chat history to answer.
        Chat History:{history_text}
        Context:{context}
        Question:{query}
     
        Answer the questions clearly with responsible AI practices.

    """
    response =groq_client.chat.completions.create(
          model ="llama-3.3-70b-versatile",
          temperature=0,
          messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content

def get_chatbot_response(query,chat_history=None):

    context = retrieve_context(query)

    answer =ask_llama(context,query,chat_history)

    return answer



