from itertools import cycle, count

for i in count(start=3, step=1):
    if i > 10:
        break
    else:
        print(i)

my_list = ['asd', 1, 2, 42, 22, 'qwe']
q = 0
for el in cycle(my_list):
    if q > 10:
        break
    print(el)
    q += 1

