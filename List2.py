# # Reverse a list in python
a=[1,2,3,4,5]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)

# # Concatenate two lists
a=['1','2','3','4','5']
b=['a','s','d','f','g']
c=[]
for i in range(0,len(a)):
    c.append(a[i]+b[i])
print(c)

# # turn Every item of a list into its square
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range(len(a)):
    b.append(a[i]**2)
print(b)


# # Remove empty strings from list of strings
a=['','adc','sdf','asdf','','']
b=[]
for i in range(len(a)):
    if a[i]!='':
        b.append(a[i])
print(b)

# # iterate both lists simultaneously
a=['1','2','3','4','5']
b=['a','s','d','f','g']
c=[]
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)

# # Add new item to list after a specified item
a=[1,2,3,4,5]
b=int(input("Enter the number to be added:"))
c=int(input("Enter the number after which to add:"))
d=[]
for i in range(len(a)):
    d.append(a[i])
    if a[i]==c:
        d.append(b)
print(d)

# # Extend nested list by adding the sublist
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[10,11,12]
c=[]
for i in range(len(a)):
    c.append(a[i])
    if a[i]==[4,5,6]:
        c.append(b)
print(c)

# Replace list’s item with new value if found
a=[1,2,3,45,5]
b=int(input("Enter the number to be replaced:"))
c=int(input("Enter the number to be replaced with:"))
d=[]
for i in range(len(a)):
    if a[i]==b:
        d.append(c)
    else:
        d.append(a[i])
print(d)

# # Remove all occurrences of a specific item from a list
a=[1,2,3,4,5,1,2,3,4,5]
b=int(input("Enter the number to be removed:"))
c=[]
for i in range(len(a)):
    if a[i]!=b:
        c.append(a[i])
print(c)