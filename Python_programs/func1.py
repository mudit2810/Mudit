# functions in python 
# A function is a block of code that performs a specific task whenever it is called. 
# In bigger programs, where we have large amounts of code, it is advisable to create or 
# use existing functions that make the program flow organized and neat.

# There are two types of functions:

# Built-in functions : min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
# User-defined functions

def average(a,b):
    print("the average is",(a+b)/2)

average(2,3)

# basic function to calculate average

# function with Default Arguments
def averagewithdefarg(a=9,b=1):
    print("the average is",(a+b)/2)

averagewithdefarg()
averagewithdefarg(5)
averagewithdefarg(b=5)
averagewithdefarg(2,3)

# function with Required arguments
def sumof2no(a,b):
    print("sum of two numbers",a+b)

#sumof2no() #TypeError: sumof2no() missing 2 required positional arguments: 'a' and 'b'
sumof2no(5,6) # here a,b are required args

# function with Variable-length arguments

def avgofnnums(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print(f"average of {len(numbers)} num",sum/len(numbers))

avgofnnums(1,2,3,4,5)

# funtion with Keyword Arbitrary Arguments

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

# function with return statement

def averagewithret(a,b):
    # print("the average is",(a+b)/2)
    return (a+b)/2

c = averagewithret(2,3)
print(c)
