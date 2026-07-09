import docx2txt
import os 

def load_docx(file_path):
    text =docx2txt.process(file_path)

    return[{
         "file_name":file_path,
         "text": text

    }]