class Solution(object):
    def missingNumber(self, nums):
       x = set(nums)
       for num in range(len(nums)+1):
        if num not in x:
            return num 