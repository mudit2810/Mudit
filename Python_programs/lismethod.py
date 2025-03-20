l = [2,1,6,0,5,0]
l.sort()
print(l)
l.append(9)
print(l)
l.remove(0)
print(l)
print(l.count(0))
l.insert(0,4)
print(l)
print(l.index(5))
l.pop(4)
print(l)
l1 = [56,20]
l.extend(l1)
print(l)
# l.reverse()
# print(l)
# l2 = l
# print(l)
# print(l2)
# l2[0] = 100
l2 = l.copy()
l2[0] = 100
print(l2)
print(l) # in python variable taking the refrence from the value if l1 and l2 both pointing to same value
# that means if we changing l2 changes should be reflect in l as well
# to avoid this we copy()
