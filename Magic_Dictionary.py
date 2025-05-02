# MAgic Dictionary
magic_dict = {"hello": 1, "worl": 1, "magic": 1, "appple": 1}
word = input("Enter word to search: ")
found = False
for key in magic_dict:
    if len(key) == len(word):
        count = 0
        for i in range(len(key)):
            if i < len(word) and key[i] != word[i]:
                count += 1
        if count == 1:
            found = True
            break
if found:
    print("Magic Word Found!")
else:
    print("Not Found!")
