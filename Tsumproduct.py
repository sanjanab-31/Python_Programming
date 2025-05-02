#accept tuple and return sum and prd as tuple

def sum_and_product(numbers):
    total_sum = sum(numbers)
    total_product = 1
    for number in numbers:
        total_product *= number
    return total_sum, total_product
numbers = (1, 2, 3, 4)
result = sum_and_product(numbers)
print("Input tuple:", numbers)
print("Sum and product:", result)
