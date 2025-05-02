a = int(input("Enter the number: "))
original = a
rev = 0
while a != 0:
    d = a % 10
    rev = rev * 10 + d
    a //= 10
if rev == original:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")