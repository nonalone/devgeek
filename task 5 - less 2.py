nat_nums = [7, 5, 3, 3, 2]
print(f'Рейтинг {nat_nums}')
nums = int(input('Введите новый элемент рейтинга '))
for elem in range(len(nat_nums)):
    if nat_nums[0] < nums:
        nat_nums.insert(0, nums)
    elif nat_nums[-1] > nums:
        nat_nums.append(nums)
    elif nat_nums[elem] > nums and nat_nums[elem + 1] < nums:
        nat_nums.insert(elem + 1, nums)
print(f'Новый рейтинг {nat_nums}')
