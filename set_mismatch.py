# Set mismatch
a={1, 2, 3, 4, 5}
b={4, 5, 6, 7, 8}
c=set()
for i in a:
    if i not in b:
        c.add(i)
for i in b:
    if i not in a:
        c.add(i)
print(c)
