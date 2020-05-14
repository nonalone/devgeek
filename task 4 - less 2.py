word = input('Введите одно слово или несколько слов через пробел ')
word_list = []
num = 1
for elem in range(word.count(' ') + 1):
    word_list = word.split()
    if len(str(word)) <= 10:
        print(f'{num} {word_list[elem]}')
        num += 1
    else:
        print(f'{num} {word_list[elem] [0:10]}')
        num += 1
