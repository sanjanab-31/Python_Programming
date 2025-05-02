# 6. Delete Lines From a File in Python
with open('file22.txt', 'r') as file:
    lines = file.readlines()
with open('file22.txt', 'w') as file:
    for line in lines:
        if "delete this" not in line:
            file.write(line)
