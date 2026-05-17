# default arguments
def func01(x,y):
    print("The value of x is:",x)
    print("The value of y is:",y)

func01(10,50)   

def func01(x,y=50):
    print("The value of x is:",x)
    print("The value of y is:",y)

func01(10) 

#def func01(x=10,y):
#    print("The value of x is:",x)
#    print("The value of y is:",y)

#func01(50) 

# Keyword Arguments

def func02(fname,lname,age):
    print(f"The first name is:{fname} and last name is:{lname} with the age as: {age}")

func02(lname="user02",fname='test',age=39)    


#Positional Arguments

def func03(name,id):
    print("Hello, My name is:",name)
    print("My empid is",id)

func03('testuser01',100)  
func03(101,'testuser02')   