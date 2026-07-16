from agents import agent

while True:
    query=input("User: ")

    if query.lower() =="exit":
        break
    elif query.upper() =="EXIT":
        break

    response = agent.invoke( {
     
       "messages":[
           {
             "role":"user",
             "content":query  
           }
       ]
    })

    print("\n Assistant:")
    print(response["messages"][-1].content)
    print("---------------------------------------------------------------------")