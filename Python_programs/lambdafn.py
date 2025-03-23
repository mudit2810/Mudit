# def sq(n):
#     return n*n

# print(sq(5))

sq = lambda x:x*x 
cube = lambda x:x*x*x
avg = lambda x,y:(x+y)/2
print(sq(2))
print(cube(5))
print(avg(5,3))

# we can pass lambda function as argument as well
def appl(fx,value):
    return 6 + fx(value)

print(appl(lambda x:x*x,2))