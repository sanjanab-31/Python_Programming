a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=input("Enter the operator: ")
if c=="+":
    print("The sum is",a+b)
elif c=="-":
    print("The difference is",a-b)
elif c=="*":
    print("The product is",a*b)
elif c=="/":
    print("The quotient is",a/b)
else:
    print("Invalid operator")