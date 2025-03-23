import os
import shutil
if(not os.path.exists("data")):
    os.mkdir("data")

# # creating files under folder
for i in range(1,6):
    os.mkdir(f"data/Day {i}")

# delete a file
#dir_path = "data"

# Check if the directory exists before deleting
# if os.path.exists(dir_path):
#     shutil.rmtree(dir_path)
#     print(f"Deleted directory and its contents: {dir_path}")
# else:
#     print("Directory does not exist.")