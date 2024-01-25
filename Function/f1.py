def greet (message):
    print(message)

greet("Hello World")


def sum(x,y):
    return x+y
print(sum(200,300))



def add(x,y):
   sum = x+y
   return sum
print(add(10,5))



# arbitutary arguments  =variable length arguments *args AND  **kwargs


# 1) variable length arguments:- *args
def addAllNumbers(*args):
    sum=0
    for i in args:
        sum+=i
    return sum 

# input = int(input("add all Numbers="))
output=addAllNumbers(1,2,3,4,5,6,7,8,9)
print(output)


# 2) keyward in arguments:- **kwargs
def studentsInfo(**kwargs):
    for x,y in kwargs.items():
        print(x, "is" , y)

studentsInfo(name="Bishal",age = 20, stream = "science")        
studentsInfo(name="ki.", age=20, stream="science") 


def number(a:int,b:int):
    if a>b:
        print("a is greater")
    else:
        print("b is greater") 
number(-1,9)



# def seperator(firstNum,secondNum,thirdNum):
#     gap=firstNum,secondNum,thirdNum,sep="-"
#     print(gap)

# seperator(2,5,4)



# match 
def calcul(firstNum,secondNum,operator):
    if operator == "+":
        result = firstNum + secondNum
    elif operator == "-":
        result = firstNum - secondNum
    elif operator == "*":
        result = firstNum * secondNum
    elif operator == "/":
        result = firstNum / secondNum
    else:
        result = "Invalid operator"
    return result

print(calcul(5, 5, "+"))



def outerfunction():
 x=1 #variable in the outer fucntion
 def innerfunction():
    y=2 #variable of inner function
    result=x+y
    return result
 return innerfunction()

print(outerfunction())


def outfun():
    a=5
    def infunc():
        b=3
        return b-a
    return infunc()
print(outfun())




# pass by reference and pass by function 

# pass by value = immutable object such as numbers (integers, floats), strings, and tuples,
def myname(num):
    num += 1
    print("inside function:", num)
    return num

x = 11
x = myname(x)
print("name of me:", x)

y=99
y=myname(y)
print( "number of the y = ",y)



def modify_number(num):
    num += 1
    print("Inside function:", num)
    
x = 5
modify_number(x)
print("Outside function:", x)



def nameAdd(nam):
    name=nam+"ishal"
    print("Full name =",name)
    return name

a="b"
c=nameAdd(a)
print("full name present =",c)



# pass by reference = such as lists, dictionaries, and custom objects 
def modify_list(ist):
    ist.append(200)
    print("inside funtion=",ist)
    return ist

my_list=[1,2,3,4,5]
modify_list(my_list)
print("outside function=",my_list)

# for this logic if we hide the [return list] than it will come= none
u_list=[5,5,5,6,4,56,5]
y=modify_list(u_list)
print("ur modify function=",y)
