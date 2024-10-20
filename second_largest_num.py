nums = [1, 2, 4, 5, 2, 4, 8, 4, 6, 7, 9, 0, 1, 4, 5]

def second_largest(nums):
    nums = list(set(nums))
    nums = sorted(nums)
    print(nums[-2])
    

second_largest(nums)