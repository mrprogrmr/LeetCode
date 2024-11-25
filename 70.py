class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
    

# Test the function with an example

n = 3
solution = Solution()
result = solution.climbStairs(n)
result

"""
The selected code is a recursive function named climbStairs within 
the Solution class. This function calculates the number of distinct 
ways to climb a staircase with n steps. The function uses a base case
to handle the simplest scenarios where n is either 0 or 1, in which 
case there is only one way to climb the stairs. For any other value 
of n, the function recursively calls itself to calculate the number 
of ways to climb the stairs by either taking one step or two steps at
a time. The final result is the sum of these two possibilities."""
