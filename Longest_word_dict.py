# Longest word in dictionary
a=['apple', 'banana', 'orange', 'grape', 'kiwi']
b=''
c=0
for i in range(len(a)):
    if len(a[i])>c:
        c=len(a[i])
        b=a[i]
print(b)