# 35 Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            elif nums[i] < target and i == len(nums) - 1:
                return len(nums)
                
            
            
# Test Cases

nums = [1, 3, 5, 6, 7]
target = 7
solution = Solution()
print(solution.searchInsert(nums, target))  # Output: 2                