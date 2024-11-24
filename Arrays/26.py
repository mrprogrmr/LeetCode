#26 Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The function uses two pointers, i and j, to iterate through the list.
        j = 0 
        # The function iterates through the list and replaces the 
        # duplicate elements with the next unique element.
        for i in  range(1, len(nums)):
            # If the current element is not equal to the element at index j,
            if nums[j] != nums[i]:
                j += 1
                # The current element is assigned to the element at index j.
                nums[j] = nums[i]
                # The index j is incremented.
        return j + 1

# Test function

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution() 
solution.removeDuplicates(nums)