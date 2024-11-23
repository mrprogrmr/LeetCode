# Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sum_val = digits[i] + carry
            digits[i] = sum_val % 10
            carry = sum_val // 10
        if carry > 0:
            digits.insert(0, carry)
        return digits
    
# Test function

digits = [1, 2, 3]
solution = Solution()
solution.plusOne(digits)
