# Area of the shape using functions
def area_of_circle(radius):
    pi = 3.14
    return pi * radius ** 2
def area_of_rectangle(length, width):
    return length * width
def area_of_square(side):
    return side ** 2
def area_of_triangle(base, height):
    return 0.5 * base * height
print("Circle:", area_of_circle(5))
print("Rectangle:", area_of_rectangle(5, 10))
print("Square:", area_of_square(4))
print("Triangle:", area_of_triangle(5, 10))
