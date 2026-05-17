# String operation

str01="Learning Python"

print(str01)

#indexing

print(str01[0:10])

# negative indexing

print(str01[-1])

# Iteration over the string

for i in str01:
    print(i)

# String immutability & concatenation

str01 =str01 + " is good for career"
print(str01)


#replace
str02 = str01.replace("Python","Java")
print(str02)
print(str01)

#strip - removes the leading and trailing whitespaces

str03 = "    In the current world, we are facing a economic drop beacuse of so many factors.    "
print(str03)
print(str03.strip())


#Formatting Strings -f string
emp_name = "testuser01"
emp_id =100
emp_dept="BA"

print(f"the emp name is:{emp_name} has emp id:{emp_id} and belongs to the department {emp_dept}")

print("the emp name is:{emp_name} has emp id:{emp_id} and belongs to the department {emp_dept}")    

#Membership

print("python" in str01)
print("Python" in str01)

#Splitting of Strings
print(str01.split(" "))

#find method
print(str01.find("a"))

#join method
list01=["Apple",'Mango']

print(" ".join(list01))
print(".".join(list01))