import re

SECTION_PATTERNS= ["Logs Validation","Event Viewer Validation","UI Access Issues","Rabbit MQ Validation"]

def chunk_documents(paragraphs):
    chunks =[]
    current_section ="Logs Validation"
    buffer=[]

    for paragraph in paragraphs:

        is_heading = any(paragraph.startswith(x)
                         for x in SECTION_PATTERNS)
        
        if is_heading:

           if buffer:

             chunks.append({
                   "section":current_section,
                   "content":"\n".join(buffer)
             }) 

           current_section =paragraph 
           buffer=[]

        else:
           buffer.append(paragraph)

    if buffer:
       chunks.append({
                   "section":current_section,
                   "content":"\n".join(buffer)
             })  
       
    return chunks   