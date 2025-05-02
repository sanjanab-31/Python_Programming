l1=[2,3,41,1,3,3,6,4,7,5,22,7]
l2=[1,99,88,76,89,56,34,21]
l3=[]
l3=l1+l2
print(l3)
for i in range(len(l3)):
    for j in range(i+1,len(l3)):
        if l3[i]>l3[j]:
            l3[i],l3[j]=l3[j],l3[i]
print(l3)
