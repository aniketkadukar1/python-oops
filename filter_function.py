"""learn about filter functions..."""

nums = [2, 4, 1, 4, 8, 4, 8, 9, 0, 8, 7, 5, 1, 3, 5]

filterd_data = list(filter(lambda x : x%2 != 0, nums))
print(filterd_data)