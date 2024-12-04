# majority element
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]
    
# Test Cases

nums = [3, 2, 3]
solution = Solution()
print(solution.majorityElement(nums))  # Output: 3

nums = [2, 2, 1, 1, 1, 2, 2]

print(solution.majorityElement(nums))  # Output: 2

"""1.
nums.sort(): This line sorts the input array nums in ascending order. After sorting, all identical elements will be grouped together.
2.
n = len(nums): This calculates the length of the input array and stores it in the variable n.
3.
return nums[n//2]: This returns the element at the middle index of the sorted array.


The key insight of this solution is that if a majority element exists (which is guaranteed by the problem statement), it will always be present at the middle index of the sorted array. This is because:

The majority element appears more than ⌊n/2⌋ times.
After sorting, all occurrences of the majority element will be grouped together.
Since there are more than ⌊n/2⌋ occurrences of the majority element, it will always occupy the middle position (and potentially some positions to its left and right).


This solution has a time complexity of O(n log n) due to the sorting operation, and a space complexity of O(1) if the sorting is done in-place (which is typically the case for Python's built-in sort method for lists).

While this solution is correct and concise, it's worth noting that there are more efficient solutions with O(n) time complexity, such as Boyer-Moore Voting Algorithm, if optimization is a concern."""
