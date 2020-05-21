my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

generator = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1]]
print(generator)


# for i in range(len(my_list)):
    # if my_list[i] > my_list[i - 1]:
        # print(my_list[i])


generator1 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
a = generator1
print(a)
