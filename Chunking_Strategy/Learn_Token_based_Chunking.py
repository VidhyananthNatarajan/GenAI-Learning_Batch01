import tiktoken

encode = tiktoken.get_encoding("cl100k_base")   # Open AI tokenizer

text ="""
Artificial Intelligence is transforming industries. Machine Learning is a subset of AI.
Deep Learning uses neural networks to learn patterns from data.

Natural Language Processing helps computers understand human language.
Computer Vision enables machines to analyze images and videos.

Generative AI can create text, images, audio, and code.
It is being adopted across healthcare, finance, education, and software development.
"""
tokens = encode.encode(text)
print(tokens)

chunk_size =30  # 12 tokens per chunk
chunks=[]

for i in range(0,len(tokens),chunk_size):
       chunk_token =tokens[i:i+chunk_size]
       chunk_text = encode.decode(chunk_token)
       chunks.append(chunk_text)

      
print(chunks)

