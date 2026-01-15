# print("#")
# print("#")
# print("#")

# for i in range(3):
#     print("#")
# # print("#\n" *3, end="")

# def main():
# #     print_column(3)
#     print_row(4)
# def print_row(length):
#     print("#" * length)
#     # for _ in range(length):
    #     print("#", end="")
# def print_column(height):
#     # for _ in range(height):
#     #     print("#")
#     print("#\n" *height,end="")
# main()

def main():
    fun_square(4)

def fun_square(size):
    for  i in range(size):
        for j in range(size):
            print("#" , end="")
        print()

main()