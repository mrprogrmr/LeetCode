# 35 Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # The method uses a linear search approach, iterating through the list
        for i in range(len(nums)):
            # If the current element is equal to the target, return its index
            if nums[i] == target:
                return i
            # If the current element is greater than the target, 
            # return the index where the target should be inserted
            elif nums[i] > target:
                return i
            # If the current element is less than the target and the next element is greater than the target, 
            # return the index of the next element
            elif nums[i] < target and i == len(nums) - 1:
                return len(nums)
                
            
            
# Test Cases

nums = [1, 3, 5, 6, 7]
target = 7
solution = Solution()
print(solution.searchInsert(nums, target))  # Output: 2                