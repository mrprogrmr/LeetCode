# Single Number

class Solution(object):
    def singleNumber(self, nums):
        uniqNum = 0
        # TRaverse all elements through the loop...
        for idx in nums:
            # Concept of XOR...
            uniqNum ^= idx
        return uniqNum
    
# Testing the singleNumber function

nums = [2, 2, 3, 4, 4, 5, 5]
result = Solution().singleNumber(nums)
print(result)  # Output: 3

"""1.
uniqNum = 0: Initialize a variable uniqNum to 0. This will be used to store the result.
2.
The method then iterates through each number in the input list nums.
3.
For each number (idx) in the list, it performs an XOR operation (^=) between uniqNum and idx.
4.
The XOR operation has some interesting properties that make this algorithm work:
XOR of a number with itself is 0: a ^ a = 0
XOR of a number with 0 is the number itself: a ^ 0 = a
XOR is commutative and associative: a ^ b ^ c = c ^ b ^ a = (a ^ b) ^ c = a ^ (b ^ c)
5.
Because of these properties, when you XOR all numbers in the array:
The duplicate numbers will cancel each other out (become 0)
The single number that appears only once will remain
6.
After the loop, uniqNum will contain the XOR of all numbers, which effectively leaves only the single number that appeared once.
7.
Finally, the method returns uniqNum, which is the single number we're looking for.


This algorithm is very efficient as it runs in O(n) time complexity and uses only O(1) extra space, regardless of the size of the input array."""