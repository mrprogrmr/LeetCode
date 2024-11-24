# Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        
        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i -1] + prevRows[-1][i]
             
        prevRows.append(newRow)
        return prevRows
    
# Test the function

numRows = 5
solution = Solution()
pascalsTriangle = solution.generate(numRows)
pascalsTriangle

"""
1.
The generate method takes an argument numRows, which specifies the number of rows to generate in Pascal's Triangle.
2.
There are two base cases:
If numRows is 0, it returns an empty list.
If numRows is 1, it returns [[1]], which is the first row of Pascal's Triangle.
3.
For any other number of rows, the method uses recursion:
It calls itself with numRows - 1 to generate all the previous rows.
The result is stored in prevRows.
4.
A new row newRow is initialized with numRows elements, all set to 1. This correctly sets up the first and last elements of the new row, which are always 1 in Pascal's Triangle.
5.
The loop for i in range(1, numRows - 1): calculates the values for the middle elements of the new row:
Each middle element is the sum of the two numbers directly above it in the previous row.
newRow[i] = prevRows[-1][i -1] + prevRows[-1][i] performs this calculation.
6.
After calculating all elements, the new row is appended to prevRows.
7.
Finally, the method returns prevRows, which now includes all rows up to and including the newly calculated row.


This implementation uses a recursive approach, building the triangle from top to bottom. Each recursive call generates one less row until it reaches the base case, then it builds back up, adding a new row at each step of the recursion unwinding.

The time complexity of this solution is O(n^2), where n is the number of rows, as it needs to calculate each element in the triangle. The space complexity is also O(n^2) to store all the elements of the triangle."""