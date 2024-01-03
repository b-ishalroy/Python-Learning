# for loop 
# range (start, end, step) 

for i in range (1,11):
    print("Hello world = ", i)


for i in range (1,11,2):
    print("Hello world = ", i)


# mention sequence 
list = [20,30,40,50]
for i in list:
    print(i)



    # While Loop 
i=0
while i<10:
    print(i)    
    i +=2



# continue, it is use when x==y condition this will skip
x=4
y=0
while x>=0:
    x-=1
    y+=1

    if x==y:
        continue
    else:
        print(x,y)


# break = stop the code when condition comes
x=4
y=0
while x>=0:
    x-=1
    y+=1

    if x==y:
        break
    else:
        print(x,y)







# print the give pattern 
n=int(input("Enter number = "))
for n in range(n):
    print("*" * 5)


# see this code for end properties 
print("Hello,",end=" ")
print("World!")

for i in range (1,4,1):
    for j in range(1,6,1):
          print("*", end="")
    print()


for i in range (1,5,1):
     for j in range (1,5,1):
          print(j, end=" ")
     print()     


for x in range (1,7,1):
    for y in range(1,10,1):
        print (y, end ="")
    print()    


n= int(input("Enter Max Number"))
for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        print(j, end="")
    print()




n = int(input("Enter the value of n: "))
for i in range(1, n + 1): 
    print("*" * i)
    

    

o = int(input("Enter the value of o: "))
for i in range (1, o+1): #loop for rows
    #printing spaces
    print(" " * (o-i), end="")

    #printing digits
    for j in range (1, 2 * i):
        print(j, end="")
    print()