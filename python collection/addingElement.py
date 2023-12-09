# Adding element to a list 
# 1) append()   => add item to the end of the list
# 2) insert()   => add items in any postion 
# 3) extend()   => adding  more value

list=[50,40,10]
list.append(90)
print(list)



list1=[50,40,10]
list1.insert(2,99)
print(list1)



list2=[50,40,10]
list.extend(list2)
print(list)



# REMOVING ELEMENTS FROM A LIST 
# 1) remove()  => remove the specify item
# 2) pop()     => remove the specify index

list=["bishal","adi","amarjit","shibu"]
list.remove("adi")
print(list)

list.pop(0)
print(list)