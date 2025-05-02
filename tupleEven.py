#return even numbers from a list using tuple

def return_even_numbers(input_list):
    even_numbers = tuple(num for num in input_list if num % 2 == 0)
    return even_numbers
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_tuple = return_even_numbers(input_list)
print("Original list:", input_list)
print("Tuple of even numbers:", output_tuple)
