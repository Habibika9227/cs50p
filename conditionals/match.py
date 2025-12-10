# name=input("what is ur name? ")

# if name=="Ahmed" or name=="Ali" or name=="Abdi":
#     print("Buruburu")


# elif name=="kilo":
#     print("Tawakal2")
# else:
#     print("Who are you? ")

#Use of Match
# name=input("Enter your name: ")
# name=name.title()
# match name:
#     case "Ahmed":
#         print("Bula jamhuriya")

#     case "Ali":
#         print("Buruburu")
#     case "Khalid":
#         print("Tawakal")

#     case "Anisa":
#         print("BB1")
#     case _:
#         print("Who are you? ")
#But we can tie this a little differently.
name=input("Enter your name: ")
name=name.title()
match name:
    case "Ahmed"| "Harry"|"Halo":
        print("you live in: Burburu")
       
    case "Anisa"| "Ali" | "Kilo":
        print("BB1")
    case _:
        print("Who are you? ")
