class Calculator:

    def __init__(self,a,b):  ## constructor
        self.a=a
        self.b =b

    def summation(self): 
        print(f"The sum is:",self.a+self.b)

obj01 = Calculator(10,20)
obj01.summation()