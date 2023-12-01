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


x=4
y=0
while x>=0:
    x-=1
    y+=1

    if x==y:
        continue
    else:
        print(x,y)

