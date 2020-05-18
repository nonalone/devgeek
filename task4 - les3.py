def my_func(x, y):
    if y >= 0:
        return x ** y
    else:
        return pow(x, y)


print(my_func(int(input('Введите положительное число ')), int(input('Введите отрицательную степень '))))
