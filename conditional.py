# Take integer input and tell it is a positive or negative 
number1=int(input("Enter first number"))
if number1>0:
 print("This Number is Positive")
else:
 print("This Number is Negative") 


#  Take positive integer input and tell if it is a odd or even 
num=int(input("Enter positive number"))
if num>0:
 if num%2==0:
   print("Even Number")
 else:
  print("ODD Number")
else:
 print("write postive number")


# If cost price and selling price of an item is input through the keyboard, write a program to determine weather the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he made or loss he incurred 
costprice= int(input("Enter Cost Price = "))    
sellingprice=int(input("Enter Selling Price ="))
if sellingprice>costprice:
 print("Profit = ", sellingprice-costprice)
elif sellingprice<costprice:
 print("Loss = ", costprice-sellingprice)
else: 
    print("No Profit-No Loss")


# Multiple condition using and - or 
eng_mark=int(input("Enter English Marks = "))     
math_mark=int(input("Enter Math Marks = "))
if eng_mark and math_mark >80:
 print("Grade = A+")
elif eng_mark or math_mark>80:
 print("Grade = B") 
else:
 print("Pass")