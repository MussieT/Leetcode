class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = prices[0]
        max_profit = 0

        # check if there is a stock less than the current.
        # subtract the current stock to the minimum stock and handle the max.
        for stock in prices:
            max_profit = max(max_profit, stock - left)
            if stock < left:
                left = stock
            
        print(max_profit)
theClass = Solution()
theClass.maxProfit([7,6,4,3,1])