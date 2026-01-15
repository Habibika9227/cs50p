
name=[]

with open("name.txt") as file:
    for lines in file:
        name.append(lines.rstrip())

    for names in sorted(name):
        print(f"{names}")


    
    
    