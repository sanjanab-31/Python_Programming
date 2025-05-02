a={'a':111,'v':11,'f':32}
print(len(a))
print(str(a))
print(type(a))
print(a.keys())
print(a.values())

y=a.copy()
print(y)
print(id(a))
print(id(y))

a.popitem()
print(a)

print(sorted(a.items(),key=lambda x:x[1],reverse=True))

y=a.setdefault('a',2222)
print(y)

keys=['a','e','i','o','u']
value="Vowel"
a=dict.fromkeys(keys,value)
print(a)

keys=['a','e','i','o','u']
value=['1','2','3','4','5']
a=dict.fromkeys(keys,value)
print(a)

# write a program to count the number of times a character appears in a given string using dictionary
# Create  dictonary for month ans noofdays for a year.User is asked to entermoth name and system will show no of days of that month
# create a dictionary to store four student details with rollno,name ,age feild.Seaaarch student in a list
