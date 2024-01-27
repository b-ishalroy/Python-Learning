# try:

     # Code that may raise an exception

# except ExceptionType:

     # Code to handle the exception

# finally:

     # Code that will be executed regardless of whether an exception occurred or not

a=int(input("Enter the first number="))
b=int(input("Enter the second number="))

try:
    result=a/b

except ZeroDivisionError:
    result= None
    print("Error:Cannot divide by zero")    

finally:
    print("Divison completed=",result)
