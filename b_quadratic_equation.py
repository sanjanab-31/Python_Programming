import math as m
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=b*b-4*a*c
if d>0:
    print(-b+m.sqrt(d)/2*a)
    print(-b-m.sqrt(d)/2*a)
elif d==0:
    print(-b/2*a)
else:
    print("No real roots")