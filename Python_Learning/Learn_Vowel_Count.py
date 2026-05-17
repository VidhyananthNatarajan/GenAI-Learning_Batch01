#Vowel count = a,e,i,o,u
text = str(input("Enter the string:"))

#text input: LearningPython
count=0

for i in text:
    if i in "aeiou":
       count =count+1 

print(count)