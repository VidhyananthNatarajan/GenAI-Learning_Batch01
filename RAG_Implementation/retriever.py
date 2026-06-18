import chromadb
from sentence_transformers import SentenceTransformer

from rank_bm25 import BM25Okapi
from config import *

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path = CHROMA_PATH)
collection = client.get_or_create_collection(COLLECTION_NAME)

def vector_search(query):
    query_embedding = embedding_model.encode(query).tolist()  
    results= collection.query(
      query_embeddings=[query_embedding],
      n_results=TOP_K
    )

    return results["documents"][0]

def bm25_search(query):
    data = collection.get()
    docs =data["documents"]
    tokenized_docs=[doc.split() for doc in docs]

    bm25 =BM25Okapi(tokenized_docs)
    scores = bm25.get_scores(query.split())

    ranked = sorted(zip(docs,scores),
           key =lambda x:x[1],
           reverse=True           
           )
    
    return[x[0] for x in ranked[:TOP_K]]


def retrieve(query):
    vector_docs = vector_search(query)
    bm25_docs = bm25_search(query)
    merged =[]

    for doc in vector_docs + bm25_docs:
        if doc not in merged:
            merged.append(doc) 

    return merged[:TOP_K]





