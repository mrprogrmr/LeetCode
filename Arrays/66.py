# Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse the list from right to left,
        for i in range(len(digits) - 1, -1, -1):
            # if the current digit is 9, set it to 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # Otherwise, increment the current digit and break the loop
                digits[i] += 1
                return digits
        return [1] + digits  # If all digits were 9, add a new 1 at the beginning of the list
    
# Test function

digits = [1, 2, 3]
solution = Solution()
solution.plusOne(digits)
