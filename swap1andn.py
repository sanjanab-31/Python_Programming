#swaping fist and last using tuple

def swap_first_and_last(input_list):
    if len(input_list) < 2:
        return input_list
    first, *middle, last = input_list
    return [last] + middle + [first]
input_list = [1, 2, 3, 4, 5]
output_list = swap_first_and_last(input_list)
print("Original list:", input_list)
print("List after swapping first and last elements:", output_list)
