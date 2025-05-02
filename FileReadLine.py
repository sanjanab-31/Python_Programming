# 5. Read Specific Lines From a File in Python
with open('file22.txt', 'r') as file:
    lines = file.readlines()
    print(lines[0])  