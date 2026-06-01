import spacy

# Load spacy English Model
nlp = spacy.load("en_core_web_sm")

text ="""
AI is transforming industries.
ML is a subset of AI.
Deep learning uses neural networks.
Natural Language Processing enables machines to understand text.
Computer Vision helps machines interpret images.
"""

docs = nlp(text)

sentences = [sent.text for sent in docs.sents]
chunk_size =3  # 2 Sentences per chunk
overlap =1
chunks=[]

for i in range(0,len(sentences),chunk_size-overlap):
       chunk =sentences[i:i+chunk_size]
       chunks.append(''.join(chunk))

print(chunks)