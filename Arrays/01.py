#1 TwoSum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # The function iterates through the list of numbers.
        number_map = {}
        # The function creates a dictionary where the keys are the numbers in the list        
        for i, num in enumerate(nums):
            # The function checks if the difference between the target and the 
            # current number exists in the dictionary.
            diff = target - num
            # If the difference exists, the function returns the indices of the two numbers.
            if diff in number_map:
                return [number_map[diff], i]
            # If the difference does not exist, the function adds the current number to the dictionary.
            else:
                number_map[num] = i
            
        return        
# Testfunction

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
solution.twoSum(nums, target)