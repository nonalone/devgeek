def my_sum(*args):
    sum_arg = 0
    stop = False
    while stop == False:

        number = input('Введите числа через пробел или q для остановки программы ').split()
        result = 0

        for elem in range(len(number)):
            if number[elem] == 'q' or number[elem] == 'Q' or number[elem] == 'й' or number[elem] == 'Й':
                stop = True
                break
            else:
                result = result + int(number[elem])
        sum_arg = sum_arg + result
        print(f'Текущая сумма {sum_arg}')

    print(f'Ваша общая сумма равна {sum_arg} ')

print(my_sum())