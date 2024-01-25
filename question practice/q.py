# Write a python function to calculate the factorial of a number (a non negative integer. the function accepts the number as an argument) 
def factorial_number(n):
    ans=1
    if n==0:
        ans = 1
    else:
        for i in range(1,n+1):
            ans*=i
        return ans
        
n=int(input("Enter first number="))        
output=factorial_number(n)
print("The factorial number is=",output)



n=int(input("Enter number="))
answer=1
for i in range (1,n+5):              #logic behind this code = 2*3*4*5*6 =720 (when inpur of n is 2)
    answer*=i
print(answer)





