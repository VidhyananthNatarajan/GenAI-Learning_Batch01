
#simple function
def add_one(i):
    return i+1

fn_lambda = lambda y:y+10 ## add the given input by 10


print(add_one(1))
print(fn_lambda(5))

# Runnable (wrapper mode)
from langchain_core.runnables import RunnableLambda
run = RunnableLambda(fn_lambda)

print(run.invoke(5))