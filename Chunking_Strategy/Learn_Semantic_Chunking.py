from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    'AI is transforming industries.',
    'Machine learning is a subset of AI.',
    'I love cooking pasta.',
    'Italian recipes are delicious.'
]

embeddings = model.encode(sentences)
chunks =[]
current_chunk = [sentences[0]]
# Similarity >= 0.5 same chunk (shares the similar meaning), <0.5 new/different one (shares the different meaning)

threshold =0.5

for i in range(1,len(sentences)):

    similarity = cosine_similarity (
        [embeddings[i-1]],[embeddings[i]]
    )[0][0]

    if similarity < threshold:
        chunks.append(current_chunk) 
        current_chunk =[sentences[i]]
    else:
        current_chunk.append(sentences[i])

chunks.append(current_chunk)

print(chunks)