
lst = [1,2,3,4,52,3,1,13,4,5,6,7,8,9,9,99]
result = []
for item in lst:
    if item not in result:
        result.append(item)
print(result)


