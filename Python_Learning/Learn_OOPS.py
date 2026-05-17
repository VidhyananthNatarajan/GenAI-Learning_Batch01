# class, Object and Function are related

class Emp_details:

    def __init__(self,name,id):  ## constructor
        self.name=name
        self.id =id

    def details(self): 
        print(f"Emp name is:{self.name}")
        print(f"Emp id is:{self.id}")

obj01 = Emp_details("testuser01",100)
obj01.details()