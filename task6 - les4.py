from math import factorial
from itertools import count

def generator():
    for el in count(4):
        yield factorial(el)

g = generator()
q = 0
for i in generator():
    if q < 5:
        print(i)
        q += 1
    else:
        break
