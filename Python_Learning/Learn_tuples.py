tup01=(56,45,"Test","Sample",78.23)
print(tup01)
print(type(tup01))

# Indexing & Silcing
print(tup01[1:4])
print(tup01[3])

# access using for loop

for i in tup01:
    print(i)

#negative indexing
print("Negative Indexing",tup01[-3])  

# updating the tuples
list01 =list(tup01)
print(list01)
print(type(list01))

# adding the elements to the list
list01.append(13)
list01.append(67.09)
print(list01)

# convert this list to tuples
tup01 =tuple(list01)
print(tup01)
print(type(tup01))


# tuple operation
tup02=(56,12,90,"Mango",23.45)

print(tup01+tup02)

#repitition
print(tup01*2)
print(tup02*3)

# Membership operator
if 12 in tup02:
   print("Given Number is a member")
else:
   print("Gvien Number is not member")  

# count property
print(tup02.count(56))
print(tup02.count(23.4))

#Length of the tuple
print(len(tup01))

#Min & Max
#print(max(tup01))

tup03=(100,456,234,109.87)
print(max(tup03))
print(min(tup03))