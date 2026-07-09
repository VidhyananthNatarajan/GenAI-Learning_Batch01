from retriever import get_chatbot_response

chat_history=[]

print("RAG Backend chat. Type exit to quit the chat")

while True:
    q=input("User: ")

    if q.lower() in {"exit","quit"}:break
    chat_history.append({"role":"user","content":q})
    try:
         ans=get_chatbot_response(q,chat_history) 
    except Exception as e:
         ans =f"Error: {e}"  
    print("Assistant:",ans)
    chat_history.append({"role":"assistant","content":q})