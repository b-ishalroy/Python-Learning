def factorial(n):
    # base case 
    if n==0:
        return 1
    
    # recursive case 
    ans=n*factorial(n-1)
    return ans

print(factorial(4))



def print_1_to_n(n):
    #base case
    if n==0:
     return
    
    print(n)
    #recursive case
    print_1_to_n(n-1)
    print(n)
   
print_1_to_n(6)

    

# write a program to print sum from 1 to n 
# input=5   &  output=15 
def input_number(n):
#    base case 
   if n==1:
      return 1
   #recursive case
   ans=n+input_number(n-1)
   return ans

n=int(input("Enter the number ="))
print(input_number(n))
   

#    Make a function which calculates the factorial of n using recursion.
def factorial_recursion(n):
   #base case
   if n==0:
      return 1
   #recursive case
   fctrial=n*factorial_recursion(n-1)
   return fctrial

n=int(input("Enter the first number of factorial="))
print(factorial(n))



# make a function that calculates "a" raised to the power "b" using recursion 
def exponent_recursion(a,b):
   #base case
   if b==0:
      return 1
   #recursive case
   exponent_function=a**b
   return exponent_function

a=int(input("Enter the number of a ="))
b=int(input("Enter the number of b="))
print(exponent_recursion(a,b))
    