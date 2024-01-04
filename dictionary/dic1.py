# dictionary = we store key value 

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