# dictionary operations

dict01={"empId":100,"empname":"testuser01","dept":"BA"}
print(dict01)
print(type(dict01))

# Accessing the dictionary

#iterate over keys
for key in dict01:
    print(key)

#iterate over values
for value in dict01.values():
    print(value)  


# iterate over keys and values      
for key,value in dict01.items():
    print(f"the key is:{key}: and the value is:{value}")

# adding the dictionary values
dict01["age"]=35
print(dict01)

dict01["salary"]=20000
print(dict01)

#delete using pop method

dict01.pop("salary")
print(dict01)

#using popitem method
dict01.popitem()
print(dict01) 


# creating dictionary with multiple elements
dict02={"empId":[100,101,102,103],
        "empname":["testuser01","testuser02","testuser03","testuser04"],
        "dept":["BA","Dev","Test","Test"]}

print(dict02)

print(dict02.keys())

print(dict02.get("empId"))

print(dict02.get("empname"))

#Copy

import copy
dict03={'a':1, 'b':[45,12,93]}
print(dict03)

#shallow copy
dict04= copy.copy(dict03)
print(dict04)

#deep copy
dict05=copy.deepcopy(dict03)
print(dict05)
