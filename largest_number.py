nums = [2, 4 ,9, 12, 1, 4]

def larget_num(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest
print(larget_num(nums))