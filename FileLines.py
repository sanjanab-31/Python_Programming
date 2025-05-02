# 3. Python Count Number of Lines in a File
with open('file22.txt', 'r') as file:
    lines = file.readlines()
    print(f"Total Lines: {len(lines)}")