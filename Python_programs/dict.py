# Dictionaries are ordered collection of data items. They store multiple items in a single variable.
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

dic = {'sid':45,'sname':'Mudit','sage':25}

print(dic)
print(type(dic))

print(dic['sname'])
print(dic['sid'])
# diff b/w both is one throw error if there is no key---other .get() return None
print(dic.get('sname'))

print(dic.values())

print(dic.keys())

for i in dic.keys():
    # print(dic[i])
    print(f"the corresponding value of key {i} is {dic[i]}")

print(dic.items())

for key,value in dic.items():
    print(f"the corresponding value of key {key} is {value}")


##### Method of dict #########

dic['gender'] = 'Male'
print(dic)
dic.update({'phone no':885558})
print(dic)

# dic.clear()
# print(dic)

dic.pop('phone no')
print(dic)

# dic.popitem()
# print(dic)

# del dic
# print(dic) ##NameError: name 'dic' is not defined

del dic['gender']
print(dic)

dic1 = {'gender':'male','Country':'India'}
print(dic,dic1)
# print(dic+dic1) TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
dic.update(dic1)
print(dic)
print(dic1)
