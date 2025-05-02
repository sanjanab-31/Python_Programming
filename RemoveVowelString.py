fruits=["apple","banana","cherry","kiwi","mango"]
for i in range(len(fruits)):
    for j in 'aeiou':
        fruits[i]=fruits[i].replace(j,'')
print(fruits)
