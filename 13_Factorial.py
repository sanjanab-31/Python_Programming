a=int(input("Enter a number: "))
fact=1
if a<0:
    print("Factorial does not exist for negative numbers")
elif a==0 or a==1:
    fact=1
else:
    for i in range(1,a+1):
        fact=fact*i
    print("Factorial of",a,"is",fact)


# import math
# a=int(input("Enter a number: "))
# print("Factorial of",a,"is",math.factorial(a))