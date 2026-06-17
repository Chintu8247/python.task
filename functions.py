def greet(name):
    print("Hello,", name + "! Welcome.")

greet("Vinay")

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(result)



def calculate_area(length, width):
    return length * width

area = calculate_area(5, 4)
print("Area:", area)


def is_even(number):
    return number%2==0
print(is_even(8))
print(is_even(1))

def get_max(numbers):
    return max(numbers)
print(get_max(2,3,4,4))