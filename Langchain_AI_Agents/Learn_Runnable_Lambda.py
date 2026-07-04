from langchain_core.runnables import RunnableLambda

def do_uppercase(text):
    return text.upper()

run = RunnableLambda(do_uppercase)
result = run.invoke("gen-ai Learning")
print(result)

## Multiple Functions

def add_msg(text):
    return text+ "!!!*&^"


chain = RunnableLambda(do_uppercase) |RunnableLambda(add_msg)

result = chain.invoke("I am doing great")

print(result)
