name = "Mudit"
print("Hello " + name , "Hello" , name)
print("Hello " ,name)

# str can we represent both in single and double quotes

add = '''
hi my name is "Mudit" 
and I am from guna 
and working in cts 
      '''

print(add)

# If you want to access element of string 
# so basically string are like array of characters with the help of indexing we can acces

print(name[0])
print(name[1])
print(name[2])
print(name[3])

# with the help of loops we can also access
for ch in name:
    print(ch)

for word in add:
    print(word)
