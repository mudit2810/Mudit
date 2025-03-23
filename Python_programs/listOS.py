import os 
folders = os.listdir("data")

print(folders)

print(os.getcwd())
os.chdir("/Mudit")
print(os.getcwd())

# print(os.listdir("F:\Mudit\data"))

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
