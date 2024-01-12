# dictionary = we store key value 

# "key" : "value"

phones={
    "john":15467,
    "born":5645448,
    "torn":551555,
    "korn": 542378
}

print(phones)
print(phones["john"])
print (phones.keys())
print(phones.values())

phones["john"]=7896
print(phones)


phones["Bishal"]=6009340989
print(phones)

phones.pop("torn")
print (phones)

# phones.clear()
# print(phones)

for x in phones:
    print(phones[x])

print(phones.items())

for x,y in phones.items():
    print(x,y)



classroom={
    "class1":{
        "Name":"Bishal",
        "Tittle":"Roy",
        "Phone Number":60093,
        "Year":2023
    },
    "class2":{
        "Name":"ad",
        "Tittle":"Rddoy",
        "Phone Number":60093,
        "Year":2023
    },
    "class3":{
        "Name":"mmshal",
        "Tittle":"saha",
        "Phone Number":54,
        "Year":2025
    }
}    

print(classroom)
print(classroom["class2"])
print(classroom["class3"]["Year"])



this_dict={
    "a":5,
    "b":7,
    "c":10
}
print(sum(this_dict.values()))
print(this_dict["a"] + this_dict["b"] + this_dict["c"])




# ***************************************************************************************
# ZIP() FUNCTION 
# zip = it helps to make one value from two iterable value 


#  Given a string and a number N, we need to mirror the characters from the N-th position up to the length  of the string in alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on 
inputString= input("Enter the string :")
n=int(input("Enter the value of n = "))

alphabets ="abcdefghijklmnopqrstuvwxyz"
reverse_alphabets=alphabets[::-1]

dict1=dict(zip(alphabets,reverse_alphabets))

prefix=inputString[0:n-1]
suffix=inputString[n-1:]


mirror=""
for i in range (0,len(suffix)):
    mirror=mirror+dict1[suffix[i]]


res=prefix+mirror
print ("The mirror reusult is", res)


