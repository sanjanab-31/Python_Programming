n=int(input("Enter the number :  "))
summ=0
for i in range(1,n+1):
    if i%2==0:
        summ+=i
print("sum of even numbers: ",sum)