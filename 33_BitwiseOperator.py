a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=a&b
print("The bitwise AND of the two numbers is",c)
c=a|b
print("The bitwise OR of the two numbers is",c)
c=a^b
print("The bitwise XOR of the two numbers is",c)
c=~a
print("The bitwise NOT of the first number is",c)
c=a<<2
print("The bitwise left shift of the first number is",c)
c=a>>2
print("The bitwise right shift of the first number is",c)