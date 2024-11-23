#27 Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

# Testing the removeElement function

nums = [3, 2, 2, 3]
val = 3
result = Solution().removeElement(nums, val)
result

