# while True:
#     user_input=int(input("Enter a value of x: "))
#     if user_input>0:
#         break 

# for value in range(user_input):
#     print("meow!")
#List:an ordered collection of elements that supports different data types.

# names=["AHmed","Ali","Anad","Ali"]
# print(name[0])
# print(name[1])
# print(name[2])
# for name in range(len(names)):
#     print(name+1,names[name])

# for name in names:
#     print(name)

#Use of dic
# names=["AHmed","Ali","Anad","Ali"]
# houses=["Buruburu","Geneva","Bula power","Buruburu"]
# print(names[0],":",houses[0])

# names={
#     "Ahmed":"Gryfindoor",
#     "Ali":"Gryfindoor",
#     "Asha":"Gryfindoor",
#     "Deco":"Slytherin",
# }
# for student in names:
#     print(student,names[student], sep=",")
# # print(names["Ahmed"])
# print(names["Ali"])         # Can be improved a little bit.
# print(names["Asha"])
# print(names["Deco"])


# for pple in range(len(names)):
#     print(pple+1,":",pple)


students=[
    {'name':'Ahmed','house':'Gryfindoor','patronus':'Otor'},
    {'name':'Ali','house':'Gryfindor','patronus':'stag'},
    {'name':'Abdi','house':'Gryfindor','patronus':'Jack Ressel Terir'},
    {'name':'Anis','house':'Sletherin','patronus':None},
]

for i in students:
    print(i["name"],i['house'],i['patronus'],sep=',')