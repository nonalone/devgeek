def div(*args):
    try:
        x = int(input("Введите делимое "))
        y = int(input("ВВедите делитель "))
        result = (x / y)
    except ValueError:
        return 'Введите цифру'
    except ZeroDivisionError:
        return "Нельзя делить на 0"

    return result
print('%.1f' % div())