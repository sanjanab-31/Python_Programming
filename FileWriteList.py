# 7. Writing List to a File in Python
data = ['Line 1', 'Line 2', 'Line 3']
with open('file22.txt', 'w') as file:
    for item in data:
        file.write(item + ',')