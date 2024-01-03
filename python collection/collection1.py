# Lists => these allow us to store multiple items in a single variable 
fruits = ["apples","bannana","mango"]
print (fruits[1])
print(type(fruits))
print(len(fruits))
print (len(fruits[1]))
# checking the item present in the list 
if "mango" in fruits:
    print("mango present in the fruits")
# checking the item not present in the list 
if "kiwi" not in fruits:
    print("kiwi not present in the fruits")


print(fruits[-3]) #apples
print(fruits[-2]) #bannana
print(fruits[-1]) #mango


#fruits[starting : ending]
print(fruits[0:2])

