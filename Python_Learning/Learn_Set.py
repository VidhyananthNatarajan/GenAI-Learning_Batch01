# set operations

set01={89,23,189,"Apple","Fruit",23.90,89}
print(set01)
print(type(set01))

# adding the items to the set
set01.add(45)
print(set01)

#updating the items to the set
#set01.update(89,123)
#print(set01)

# discard and remove method
set01.discard("Fruit")
print(set01)

set01.discard("Fruit")
print(set01)

set01.remove(189)
print(set01)

#set01.remove(189)
#print(set01)

#union of 2 sets
print("Set01 is:",set01)
set02 ={"Check",88.10,90,23}
print("Set02 is",set02)
#print(set01.union(set02))

#Intersection o2 sets

#print(set01.intersection(set02))

#intersection update
#print(set01.intersection_update(set02))

#set difference
print(set01 -set02)
print(set02 -set01)

#symmetric difference
print(set01.symmetric_difference(set02))

#set comparisons

print(set01 !=set02)

print(set01 == set02)
print(set01 > set02)
print(set02 > set01)

#length comparison
print (len(set01) > len(set02))
print (len(set01) == len(set02))

#set to list

list01 = list(set01)
print(list01)
print(type(list01))