a=int(input("Enter the number: "))
rev=0
while a!=0:
    rev=rev*10+a%10
    a=a//10
print("Reverse of the number: ",rev)