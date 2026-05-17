# Exception handling division by zero

try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    print(num1//num2)
except ZeroDivisionError:
    print("Exception occured.Can't divide by Zero. Change the Denominator.")   
finally:
    print("Execution was completed successfully")     

