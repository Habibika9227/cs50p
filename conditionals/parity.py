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
    else:
        return False
    
main()