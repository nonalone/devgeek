
def my_func(*args):
    x = int(input("Введите первое число "))
    y = int(input("ВВедите второе число "))
    z = int(input("ВВедите третье число "))

    if x >= z and y >= z:
        return x + y
    elif x > y and x < z:
        return x + z
    else:
        return y + z

print(my_func())


