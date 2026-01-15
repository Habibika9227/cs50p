def main():
    name=input("whats ur name? ")
    data=hello(name)
    print(data)

def hello(to="world"):
    return f"hello,{to}" 

if __name__=="main":
    main()
