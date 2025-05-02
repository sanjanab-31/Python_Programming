# 4. Python Search for a String in Text Files
search_string = "is"
with open('file22.txt', 'r') as file:
    for line in file:
        if search_string in line:
            print(line.strip())