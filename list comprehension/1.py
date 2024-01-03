# it is use when we want to make a new list from items of an existing list 
list = [20,40,8,30,82]
for i in list:
    print (i)


name=["bishal", "adi", "amit", "sagar","dipankar"]
for names in name:
    print(names)


names=["Bishal","ayantika","Love"]
new_name= [name for name in names if "a" in name]
print(new_name)



# nested list 
numb = [10,[20,30],40]
print(numb[0])
print(numb[1])
print(numb[1][0])
print(numb[1][1])
print(numb[2])




# swapping value 
n= int (input("Enter the size of the number= "))
list=[]
for i in range(n):
    num=int(input("Enter all the number = "))
    list.append(num)




fruits=("bannana", "apple","lemon")
for fruit in fruits:
    print(fruit)
print(len(fruit))



students = ("Bishal", "Adi", "Amarjit")

if "Bishal" in students:
  index = students.index("Bishal")  # Get the index of "Bishal"
  print(f"Yes, Bishal is present at index {index}")
  print("Bishal is present in this index", index)

print(students[0])
print(index)


# union function 
set1 = {"Bishal","Adi","Amarjit","Arijit"}
set2={1,2,3,4,5,6}
set3=set1.union(set2)
print(set3)

set1.update(set2)
print(set1)
 

def greet(name):
    """Greets a person by name."""
    print("Hello, " + name + "!")

# Call the function
greet("Bishal")  # Output: Hello, Alice!



# Print the maximum aRd miRimum elemeRt iR a set in Python 
set = [1,2,3,5,6,77]

minset= min(set)
maxset= max(set)

print(minset)
print(maxset)

#  GiveR three arrays, we have to find common elemets iR three sorted lists using sets.  

ar1={1,5,9,11,15}
ar2 = {2,1,6,11}
ar1.intersection_update(ar2)
print(ar1)

