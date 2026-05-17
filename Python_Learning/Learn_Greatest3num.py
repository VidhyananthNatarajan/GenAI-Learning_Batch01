# Greatest of 3 numbers. X,Y,Z

x = int(input("Enter the value for x:"))
y = int(input("Enter the value for y:"))
z = int(input("Enter the value for z:"))

if (x>y) and (x>z):
    print("x is greatest")
elif y>z: 
    print("y is greatest")   
else:
    print("z is greatest")    