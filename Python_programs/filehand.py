# READING A FILE
# f = open('F:\Mudit\Python_programs\myfile.txt','r')
# #print(f)
# text = f.read()
# print(text)
# f.close()

#WRITING A FILE
# f = open('myfile2.txt','w')
# f.write("Hi you are new file")

# f = open('F:\Mudit\Python_programs\myfile.txt','w')
# f.write("Hi you are new file")
# f.close()

# append content to the file

# f = open('F:\Mudit\Python_programs\myfile.txt','a')
# f.write("appended content")
# f.close()

# USING WITH CLAUSE
# with open('F:\Mudit\Python_programs\myfile.txt','a') as f:
#     f.write("appned content with clause")

# with open('F:\Mudit\Python_programs\myfile.txt','r') as f:
#     text = f.read()
# print(text)
    
### readline writeline methods

# f = open('myfile2.txt','r')
    
# while True:
#     # line = f.readline()
#     # print(line)
#     lines = f.readlines() # convert into list of lines
#     for line in lines:
#         print(line)
#     if not lines:
#         break
    
f = open('myfile3.txt','r')
i = 0
while True:
    i+=1
    line = f.readline()
    marks = line.split(',')
    if not line:
        break
    print(f"Marks of student {i} in maths:{marks[0]}")
    print(f"Marks of student {i} in evs:{marks[1]}")
    print(f"Marks of student {i} in ss:{marks[2]}")

f = open('myfile4.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
