# Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

# Testing the maxProfit function

prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
solution.maxProfit(prices)  # Output: 5

"""
1.
buy = prices[0]: Initialize the buying price to the first price in the list. This assumes we start by considering buying on the first day.
2.
profit = 0: Initialize the maximum profit to 0.
3.
for i in range(1, len(prices)):: Iterate through the prices starting from the second day (index 1) to the last day.
4.
Inside the loop, there are two main conditions:

a. if prices[i] < buy:: If we find a price lower than our current buying price, we update buy to this lower price. This is because we want to buy at the lowest possible price.

b. elif prices[i] - buy > profit:: If selling at the current price would yield a profit higher than our current maximum profit, we update the profit. This is calculated by subtracting the buying price from the current price.
5.
return profit: After checking all prices, return the maximum profit found.


This algorithm efficiently solves the problem in O(n) time complexity, where n is the number of prices, by making a single pass through the array. It keeps track of the lowest price seen so far and the maximum profit that can be achieved.

The key insight is that we don't need to consider every possible pair of buy and sell days. Instead, we can always keep track of the minimum price seen so far as the potential buying day, and for each price, we calculate the profit if we were to sell on that day. If this profit is greater than the maximum profit seen so far, we update our maximum profit."""