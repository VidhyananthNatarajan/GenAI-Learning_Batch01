#List operations
list01=[67,34,89,"Apple",34.89]
print(list01)
print(type(list01))

#index
print(list01[4])

#Repetition
print(list01*3)

#Slicing
print(len(list01))

print(list01[0:5])

print(list01[0:3])

#iteration
for i in list01:
    print(i)

#concatenation - adding of two strings
list02 =[78,23,75,100,67.90,"One",23,78]   
print(list02) 
print(list01 + list02)
print(list02 + list01)

list03=list01 + list02
print(list03)

#Membership operation
print(list01)

for i in list01:
    if i in list03:
        print("Elements are the members of the group")
    else:
        print("Elements aren't the members of the group")    

print(list01.append("First"))   
print(list01)  

list01.remove(list01[4])
print(list01)

#Max and Min
#print(min(list01))

list04=[89,34,100,56,56,34]
print(min(list04))
print(max(list04))