n = input("Enter the number :")
print(f"Print the table of number {n}")

try:
    for i in range(1,11):
        print(f'{int(n)} X {i} = {int(n)*i}')
# except Exception as e:
#     print(e)
except:
    print("invalid input")

print("Imp lines")
print('end of the progrm')

try:
    n = int(input("press number"))
    a = [1,2]
    print(a[n])
except ValueError:
    print("Not a number")
except IndexError:
    print("Not an vaild index")