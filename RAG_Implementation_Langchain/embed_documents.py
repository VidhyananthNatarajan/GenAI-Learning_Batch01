import chromadb
from sentence_transformers import SentenceTransformer
from document_loader import load_docx
from chunker import chunk_text
from chromadb.config import Settings

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path = "./chroma_db")
collection = client.get_or_create_collection(name="project_docs")

def create_vector_store():
    docs = load_docx("data/SOP_doc.docx")
    chunks = chunk_text(docs)
    print(f"Chunks created:{len(chunks)}")

    for idx,chunk in enumerate(chunks):
        embedding = embedding_model.encode(chunk["content"]).tolist()   
    collection.add(
          ids=[str(idx)],
          documents=[chunk["content"]],
          embeddings=[embedding],
          metadatas=[{"source":chunk["source"]}]
    )
    print("Vector DB Creted Successfully")
    



if __name__ =="__main__":
    create_vector_store()