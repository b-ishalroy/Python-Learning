o = int(input("Enter the value of o: "))
for i in range (1, o+1): #loop for rows
    #printing spaces
    print(" " * (o-i), end="")

    #printing digits
    for j in range (1, 2 * i):
        print(j, end="")
    print()
     