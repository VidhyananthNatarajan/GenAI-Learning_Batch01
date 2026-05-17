# Multiple except blocks

try:

    list01=['Apple',45,23,67.90]
    print(list01[6])

except IndexError:
    print("Index Error: Index out of range. use len statement to get the length and use the index =max(len-1)")    

except ValueError:
    print("The input value is Invaild")    