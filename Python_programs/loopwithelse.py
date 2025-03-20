# l1 = ['name',"age"]
# l2 = ["master",25]

# d = {}
# d1 = d.fromkeys(l1,l2)
# print(d1)

# hum for loop while k sath bhi else use kar skte

for i in range(5):
    print(f'i is {i}')

else:
    print("loop successfully khatm hua")

# agar isme break dal dege toh loop successfully khtm ni hoga to else ni chalega
for i in range(5):
    print(f'i is {i}')
    if i == 3:
        break

else:
    print("loop successfully khatm hua")

i = 0
while i < 7:
    # if i == 6:
    #     break
    print(f'i is {i}')
    i+=1
else:
    print("while loop successfully khatm hua")