# Regular Expressions

import re

text = str(input("Enter the text:"))

if re.match("Hello",text):
    print("Sentence starts with Hello")
else:
    print("Sentence doesn't starts with Hello")    


# Mobile number validation 10 digits only
# 
mob_num = str(input("Enter the mobile number:"))   

if re.match("\d{10}",mob_num):
    print("Mobile number is proper")
else:
    print("Invaild mobile number")    