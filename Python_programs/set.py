# Sets are unordered collection of data items. They store multiple items in a single variable. 
# Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable,
# meaning you cannot change items of the set once created. Sets do not contain duplicate items

s1 = {1,2,3,2}
print(s1) #{1, 2, 3} removing duplicates
print(type(s1)) # <class 'set'>

# create an empty set 
s2 = set() # this is correct way s2 = {} not like this

# accessing the set element 
for i in s1:
    print(i)

s3 = {1,2,3}
s4 = {3,4,6}
print(s3.union(s4))
print(s3,s4)
s3.update(s4) # method to update a set jaise s3 ko update kar dega with union of s4
print(s3)

s5 = {1,2,3,4}
s6 = {3,4,5}
print(s5.intersection(s6))
print(s5,s6)
# s5.intersection_update(s6)
# print(s5)

#symmetric diff

print(s5.difference(s6))
print(s5.symmetric_difference(s6))

###### set methods #######
# 1. isdisjoint()  both set are different

s7 = {7,8,9}
print(s6.isdisjoint(s7)) # true
print(s5.isdisjoint(s6)) # false 3,4 are comman

# 2. issuperset()

print(s1.issuperset(s3)) # false
print(s3.issuperset(s1)) # True

# 3. issubset()
print(s1.issubset(s3)) # true
print(s3.issubset(s1)) # false






