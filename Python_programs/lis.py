lis = [44,45,55,50]

print(lis[0])
print(lis[1])
print(lis[2])
print(type(lis))
#print(lis[4]) 
print(len(lis))

#indexing

print(lis[:-1])
print(lis[:3])
print(lis[0:])
print(lis[::2])

if 4 in lis:
    print("me hoo")
else:
    print("ni hu")

lis1 = [i for i in range(0,5)]
lis2 = [i*i for i in range(0,5)]
print(lis1)
print(lis2)
lis3 = [i*i for i in range(0,10) if i%2 == 0]
print(lis3)
