#tuple of numbers  and returns a new tuple containging only those numbers which are greater than the average of the numbers in the original tuple

def greater_than_avg(input_tuple):
    avg = sum(input_tuple) / len(input_tuple)
    result_tuple = tuple(num for num in input_tuple if num > avg)
    return result_tuple
input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
output_tuple = greater_than_avg(input_tuple)
print("Original tuple:", input_tuple)
print("Tuple of numbers greater than average:", output_tuple)
