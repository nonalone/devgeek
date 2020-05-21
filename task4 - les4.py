from functools import reduce

def my_f(num1, num2):
    return num1 * num2

print(reduce(my_f, [el for el in range(100, 1001) if el % 2 == 0]))