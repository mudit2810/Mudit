# MAP

# def cube(x):
#     return x*x*x

l = [1,2,3,4]
### method to create nl using loop and cube of element but we can use map 
# nl = []
# for i in l:
#     nl.append(cube(i))

# print(nl)

#nl = list(map(cube,l))
# infact we can use lambda as well
# nl = list(map(lambda x:x*x*x,l))
# print(nl)

###### FILTER #######
l1 = 2,5,8,14,24,50
def filter_fun(n):
    return n>10
# nl1 = list(filter(filter_fun,l1))
nl1 = list(filter(lambda x:x>10,l1))
print(nl1)

### reduce
from functools import reduce

nl2 = reduce(lambda x,y:x+y,l)

print(nl2)