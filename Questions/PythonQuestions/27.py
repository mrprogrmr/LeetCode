#27 Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Using list comprehension to remove the element
        nums = [x for x in nums if x!=val]
        
        # Using a while loop to remove the element
        # i = index of current element
        # len(nums) is the length of the list after removing the element
        # If the current element is equal to the value, pop it from the list
        # Otherwise, increment the index by 1 to move to the next element
        # Repeat this process until all elements are removed or the index exceeds the length of the list
        # Return the length of the list, which will be the new length of the list after removing the element(s)

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

