#1 TwoSum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in number_map:
                return [number_map[diff], i]
            else:
                number_map[num] = i
            
        return        
# Testfunction

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
solution.twoSum(nums, target)