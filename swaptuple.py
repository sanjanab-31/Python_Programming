#swap values using tuple

def swap_values(a, b):
    a, b = b, a
    return a, b
x = 5
y = 10
swapped_x, swapped_y = swap_values(x, y)
print("Original values: x =", x, ", y =", y)
print("Swapped values: x =", swapped_x, ", y =", swapped_y)