from nltk.tokenize import word_tokenize

text ="AI is transforming industries.ML is a subset of AI. Deep learning uses neural networks."

words = word_tokenize(text)
print(words)

chunk_size =12   # 12 tokens per chunk
overlap =1
chunks=[]

for i in range(0,len(words),chunk_size-overlap):
       chunk =words[i:i+chunk_size]
       chunks.append(''.join(chunk))

      
print(chunks)
