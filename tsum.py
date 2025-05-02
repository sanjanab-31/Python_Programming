#return new tuple containing the element-wise sum of two tuples

def element_wise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length")
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return result
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = element_wise_sum(tuple1, tuple2)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Element-wise sum:", result)
