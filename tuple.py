# give tuple function in python
t=(1,2,3,4,5)
print(t)


# 1.      Write a Python program to unpack a tuple into several variables.
t=(1,2,3,4,5)
a,b,c,d,e=t
print(a,b,c,d,e)

# 2.       Write a  Python program to convert a tuple to a string.
t=('a','b','c','d','e')
s=''.join(t)
print(s)

# 3. Write a Python program to check whether an element exists within a tuple.
t=(1,2,3,4,5)
print(3 in t)


# Tuple with the same product
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=[]
# for i in range(len(l1)):
#     l3.append(l1[i]*l2[i])
# print(l3)

# Copy speccific elements from one tuple to a new tuple
# l1=(1,2,3,4,5,6,7,8,9,10)
# l2=()
# for i in range(len(l1)):
#     if i%2==0:
#         l2+=l1[i],
# print(l2)


