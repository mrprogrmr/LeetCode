class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        # Initialize the node with the given value, left child as None, and right child as None
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        # Helper function to construct the BST recursively
        def helper(arr, s, e):
            # Base case: if start index is greater than end index, return None
            if s > e:
                # Return None if start index is greater than end index
                return None
            
            # Find the middle index of the current subarray
            mid = s + (e - s) // 2
            
            # Create a new TreeNode with the value at the middle index, assign it to the current node, and recursively construct the left and right subtrees
            node = TreeNode(arr[mid])
            
            # Recursively construct the left and right subtrees of the current node
            node.left = helper(arr, s, mid - 1)
            # Recursively construct the right subtree of the current node
            node.right = helper(arr, mid + 1, e)
            
            # Return the current node
            return node
        
        # Check if the input array is empty
        
        n = len(nums)
        
        # If the input array is empty, return None
        if n == 0:
            
            return None
        
        # Construct the BST recursively and return the root node
        return helper(nums, 0, n - 1)
    
# Test function

nums = [-10, -3, 0, 5, 9]
solution = Solution()
root = solution.sortedArrayToBST(nums)
print(root.val)  # Output: 0

"""1.The method sortedArrayToBST takes a sorted array nums as input and returns the root of a height-balanced binary search tree (BST).
2. Inside sortedArrayToBST, there's a nested helper function called helper that does the main work of constructing the BST recursively.
3. The helper function takes three parameters:
arr: The input array
s: The start index of the current subarray
e: The end index of the current subarray
4.
The base case for the recursion is when s > e, which means we've processed all elements in the current subarray. In this case, we return None.
5.
To create a balanced BST, we find the middle element of the current subarray:
mid = s + (e - s) // 2
This calculation avoids potential integer overflow that could occur with (s + e) // 2.
6.
We create a new TreeNode with the value at the middle index: node = TreeNode(arr[mid]).
7.
We recursively construct the left subtree by calling helper(arr, s, mid - 1) and assign it to node.left.
8.
Similarly, we recursively construct the right subtree by calling helper(arr, mid + 1, e) and assign it to node.right.
9.
After constructing both subtrees, we return the current node.
10.
Outside the helper function, we first check if the input array nums is empty. If it is, we return None.
11.
If nums is not empty, we call the helper function with the full range of the array: helper(nums, 0, n - 1), where n is the length of nums.


This implementation ensures that the resulting BST is height-balanced because it always chooses the middle element as the root for each subtree. The time complexity of this algorithm is O(n), where n is the number of elements in the input array, as it visits each element once to construct the tree."""