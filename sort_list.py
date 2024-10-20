"""Bubble Sort Algorithm with nLog(n) time complexity"""

nums = [2, 5, 1, 5, 7, 3, 7, 2, 8, 2, 4, 0, 9]

for i in range(len(nums)-1):
    for j in range(i, len(nums)-1):
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)
