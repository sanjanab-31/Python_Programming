print("Welcome "," to "," python "," programming",sep="**")



a="welcome to python programming"
print(a.replace(" ","**"))


s=input("Enter the string:")
r=s.split(" ")
for i in r:
    print(i,end='**')


a = input("Enter a string: ")
result = ""
for i in a:
    if i == " ":
        result += "**"
    else:
        result += i
print(result)