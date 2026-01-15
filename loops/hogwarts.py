#List

# students=['Ahmed', "Ali", "Adna"]
# print(students[0])
# print(students[1])
# print(students[2])
# for i in range(len(students)):
#     print(i+1,students[i],end="")

# Dictionary:allows u to dynamically associate keys with values.
# students=['Ahmed', "Ali", "Adna",'Abdullahi']
# houses=['Gryfindor','Gryfindor','gryfindor','slytherin']
# students={"Ali":"Gryfindor" ,
#           "Abdi":"Gryfindor",
#           "Ahmed":"Gryfindor",
#           "Deco":"Slytherin",                   
# }
# print(students["Ali"])
# print(students["Abdi"])
# print(students["Ahmed"])
# print(students["Deco"])

secret_number=5
guess_count=0
while guess_count < 3:
    guess_input=int(input("Guess: "))
    # if guess_input==secret_number:

    guess_count+=1
    # print("you failed")
    if guess_input==secret_number:
        print("You won!")
        break
else:
 print("You failed!")