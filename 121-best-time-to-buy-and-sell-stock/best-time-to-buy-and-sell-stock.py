class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                temp_profit = prices[r] - prices[l]
                profit = max(profit, temp_profit)
            else: 
                l = r # found better time to buy stock 
            r += 1
        return profit 