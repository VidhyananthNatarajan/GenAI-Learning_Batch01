import os

from dotenv import load_dotenv

from groq import Groq
from retriever import retrieve
from config import *
load_dotenv()

client =Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT ="""
You are a BAU Support Engineer. Answer ONLY from SOP Context.
If answer is unavilable: Information not found in SOP.
"""

def ask_question(question):
    docs = retrieve(question)
    context ="\n\n".join(docs)
    prompt =f"""
    Context:{context}
    Question:{question}
    Answer:
    """

    response = client.chat.completions.create(
     model = LLM_MODEL,
     temperature =0,
     messages =[
       {
          "role":"system", 
          "content":SYSTEM_PROMPT

       },

       {
          "role":"user", 
          "content":prompt

       }
    ])

    return response.choices[0].message.content

def main():

    print("SOP RAG Console")

    while True:
        question = input("\nQuestion: ")
        if question.lower() in ["exit","quit"]:
            break
        answer = ask_question(question)

        print("\nAnswer:")
        print(answer)

if __name__=="__main__":
    main()        