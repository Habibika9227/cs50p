# x=int(input("enter a nuber: "))


# if x%2==0:
#     print("even")

# else:
#     print("odd")

def main():
    x=int(input("enter a number: "))
    if is_even(x):
        print("Even")

    else:
        print('odd')



def is_even(n):
    if n%2==0:
        return True
    return True if n%2==0 else False

    # else:
    #      return False
    # #more simplified version
    # return True if n%2==0  else False
    # #condenced version since value evalute true or false
    # return n%2==0

main()


