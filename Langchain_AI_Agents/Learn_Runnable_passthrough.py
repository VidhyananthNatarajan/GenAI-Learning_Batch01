from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough()
result = chain.invoke("Hi.How are you?")
print(result)