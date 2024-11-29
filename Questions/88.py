class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Merge the two sorted arrays into nums1
        i = m - 1
        j = n - 1
        # Start from the end of nums1 and nums2 and merge them into nums1
        k = m + n - 1
        # Continue merging until we reach the beginning of either nums1 or nums2
        while j >= 0:
            # Compare the last elements of nums1 and nums2
            if i >= 0 and nums1[i] > nums2[j]:
                # Move the last element of nums1 to the next position
                nums1[k] = nums1[i]
                # Move the last element of nums1 one position to the left
                i -= 1
            else:
                # Move the last element of nums2 to the next position
                nums1[k] = nums2[j]
                # Move the last element of nums2 one position to the left
                j -= 1
            # Move the last position of nums1 to the next position    
            k -= 1
# Test the solution
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

"""1.
The function takes four parameters:
nums1: The first array, which has extra space to accommodate elements from nums2.
m: The number of elements in nums1 (excluding the extra space).
nums2: The second array to be merged into nums1.
n: The number of elements in nums2.
2.
The merging process starts from the end of both arrays:
i = m - 1: Points to the last element in the filled portion of nums1.
j = n - 1: Points to the last element in nums2.
k = m + n - 1: Points to the last position in nums1 where we'll place the merged elements.
3.
The main loop while j >= 0 continues until all elements from nums2 are processed.
4.
Inside the loop, there's a comparison:
If i >= 0 and nums1[i] > nums2[j], it means the current element in nums1 is larger. This element is placed at position k in nums1, and i is decremented.
Otherwise, the current element from nums2 is placed at position k in nums1, and j is decremented.
5.
After each placement, k is decremented to move to the next position where an element will be placed.


This approach efficiently merges the arrays in-place, starting from the end. It ensures that larger elements are placed at the end of nums1, gradually filling it from right to left. This method avoids overwriting elements in nums1 that haven't been processed yet.

The time complexity of this algorithm is O(m+n), where m and n are the lengths of nums1 and nums2 respectively. The space complexity is O(1) as it modifies nums1 in-place without using any extra space.
"""





# Solution 2
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#     # Combine the two arrays into one sorted array
#       for j in range(n):
#           # Insert the next element from nums2 into nums1 at the correct position
#           nums1[m+j] = nums2[j]
#           # Move all elements from nums1[0] 
#           # to nums1[m+j-1] to make room for the new element          
#       nums1.sort()
      
# # Test the solution

# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# solution = Solution()

# solution.merge(nums1, m, nums2, n)

# print(nums1)  # Output: [1, 2, 2, 3, 5, 6]