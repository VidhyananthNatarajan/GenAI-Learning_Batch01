# madam -madam, mam-mam

str01 = str(input("Enter the string:"))

print(str01[::-1])  # variable[start,end,counter]


if str01==str01[::-1]:
    print("String is a Palindrome")
else:
    print("String is not a Palindrome")    