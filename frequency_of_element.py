"""Program to check the frequency of the element in a list"""

nums = [1, 2, 4, 5, 6, 8, 9, 6, 4, 2, 1, 5, 2, 4]

def freq_of_ele(nums):
    freq = {}
    for i in nums:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    print(freq)

freq_of_ele(nums)
        
