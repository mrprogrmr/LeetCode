#26 Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0 
        for i in  range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1

# Test function

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution() 
solution.removeDuplicates(nums)