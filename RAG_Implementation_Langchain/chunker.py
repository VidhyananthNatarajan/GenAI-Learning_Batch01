from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(documents):
    splitter =RecursiveCharacterTextSplitter(chunk_size=750,chunk_overlap=150)

    chunks=[]

    for doc in documents:
        
         texts =splitter.split_text(doc["text"])

         for chunk in texts:
              chunks.append({
                   "content":chunk,
                   "source":doc["file_name"]

              })
    return chunks