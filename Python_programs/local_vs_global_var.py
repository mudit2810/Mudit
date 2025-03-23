# """A variable is a named location in memory that stores a value. 
# In Python, we can assign values to variables using the assignment operator =. 
# For example:

# x = 5
# y = "Hello, World!"
# Now, let's talk about local and global variables.

# A local variable is a variable that is defined within a function and is only accessible within that 
# function. It is created when the function is called and is destroyed when the function returns.

# On the other hand, a global variable is a variable that is defined outside of a function and 
# is accessible from within any function in your code.
# """

x = 4 # global variable

def myfunc():
    # x = 5 # local varibale
    y = 5 # local
    global x
    x = 5

    print(f"I am local variable inside my func x:{x}")
    print(f"I am local variable inside my func x:{y}")

myfunc()
print(f"I am global varibale x:{x}") # here overwrite value global var using global keyword