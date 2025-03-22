# n = input("Enter the number :")
# print(f"Print the table of number {n}")

# try:
#     for i in range(1,11):
#         print(f'{int(n)} X {i} = {int(n)*i}')
# # except Exception as e:
# #     print(e)
# except:
#     print("invalid input")

# print("Imp lines")
# print('end of the progrm')

# try:
#     n = int(input("press number"))
#     a = [1,2]
#     print(a[n])
# except ValueError:
#     print("Not a number")
# except IndexError:
#     print("Not an vaild index")

# # https://career5.successfactors.eu/careers?company=capgemitecP3

# ## finally keyword: I am always executed whatever the condition

# # The finally code block is also a part of exception handling.When we handle exception using 
# # the try and except block, we can include a finally block at the end.
# # The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources 
# # or closing database connection or may be ending the program execution with a delightful message.

# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")
#   # print("I am always executed")


# x = func1()
# print(x)

# custom In python, we can raise custom errors by using the raise keyword.

a = input("enter number")

if a.lower() == "quit":
    print("I am quiting a program")
elif a.isdigit():
    print("I am interger")
else:
    raise ValueError("Other string are not allowed") 
