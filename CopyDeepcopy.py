# copy() and Deepcopy() example
import copy
list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
list3 = copy.deepcopy(list1)
list3[0] = 10
print("Original list:", list1)
print("Shallow copy:", list2)
print("Deep copy:", list3)
