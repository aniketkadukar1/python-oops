from functools import reduce

nums = [1, 4, 2, 7, 9, 8, 0, 3, 4, 6, 2, 1, 5, 8]

reduced_nums = reduce(lambda x, y: x+y, nums)

print(reduced_nums)