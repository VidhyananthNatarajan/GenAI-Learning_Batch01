MAX_CHUNK_SIZE = 50

def recursive_split(text):
    """
       Recursively split the input text into chunks that do not exceed MAX_CHUNK_SIZE.
       Splitting hierarchy:
       1. Paragarphs
       2. Sentences
       3. Words
    """

    if len(text) <=MAX_CHUNK_SIZE:
        return[text.strip()]
    
    chunks =[]

    # split by paragarphs
    paragraphs = text.split('\n\n')

    for para in paragraphs:
        if len(para) <=MAX_CHUNK_SIZE:
            chunks.append(para.strip())
            continue
    #split large paragraphs into sentences
        sentences = para.split('. ')
        current_chunk =""

        for sentence in sentences:
            if len(current_chunk) +len(sentence)+1 <=MAX_CHUNK_SIZE:
                current_chunk += " " +sentence if current_chunk else sentence
            else:
                if current_chunk:
                   chunks.append(current_chunk.strip())                   

         # Handle long sentences
            if len(sentence)  >= MAX_CHUNK_SIZE:
                words = sentence.split()
                word_chunk =""

                for word in words:
                    if len(word_chunk) +len(word)+1 <=MAX_CHUNK_SIZE:
                       word_chunk += " " +word if word_chunk else word
                    else:
                        chunks.append(word_chunk.strip())
                        word_chunk =word

                if word_chunk:
                   chunks.append(word_chunk.strip())         

                current_chunk =""
               
            else:
                current_chunk =sentence

    return chunks

text ="""
Artificial Intelligence is transforming industries. Machine Learning is a subset of AI.
Deep Learning uses neural networks to learn patterns from data.

Natural Language Processing helps computers understand human language.
Computer Vision enables machines to analyze images and videos.

Generative AI can create text, images, audio, and code.
It is being adopted across healthcare, finance, education, and software development.
"""   

chunks =recursive_split(text)

for i ,chunk in enumerate(chunks,start=1):
      print(f"Chunk{i}:")
      print(chunk)
      print(f"Length: {len(chunk)} characters")
      print("-"*50)
