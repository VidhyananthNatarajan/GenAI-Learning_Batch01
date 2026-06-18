import chromadb
from sentence_transformers import SentenceTransformer
from document_loader import load_docx
from chunker import chunk_documents
from config import *

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path = CHROMA_PATH)
collection = client.get_or_create_collection(COLLECTION_NAME)

def create_embeddings():
    paragraphs = load_docx("data/SOP_doc.docx")
    chunks = chunk_documents(paragraphs)
    print(f"Chunks created:{len(chunks)}")

    for idx,chunk in enumerate(chunks):
        text = f"""
        Section:{chunk['section']}
        Content:{chunk['content']}
    """
    embedding = embedding_model.encode(text).tolist()   
    collection.add(
          ids=[str(idx)],
          documents=[text],
          embeddings=[embedding],
          metadatas=[{"section":chunk["section"]}]
    )

    print(f"inserted chunk {idx} ")

print("Embedding Completed")

if __name__ =="__main__":
    create_embeddings()