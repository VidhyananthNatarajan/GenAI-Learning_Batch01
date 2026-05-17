# sum of n digits - 6764564399 -> 6+7+6+4+5+6+4+3+9+9 =59

num = 6764564399
result =0
while(num >0):
    result =result +num %10
    num = num//10   # use floor division to get the exact dividend.

print("The sum is:",result)    