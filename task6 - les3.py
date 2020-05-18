def int_func(*args):
    word = input('Введите слово с маленькой буквы ')
    print(word.title())
    # return
int_func()

def int_func1(*args):
    words = input('Введите слова через пробел ').split()
    for word in words:
        print(word.title())
    # return
int_func1()