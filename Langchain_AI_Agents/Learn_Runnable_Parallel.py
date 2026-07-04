from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel


def count_word(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def do_upper(text):
    return text.upper()

# Run all these functions at the same time 

parallel= RunnableParallel(
     word =RunnableLambda(count_word),
     chars =RunnableLambda(count_chars),
     up_case =RunnableLambda(do_upper)

 )

input_text ="I am learning Langchain concepts."

result = parallel.invoke(input_text)
print(result)




