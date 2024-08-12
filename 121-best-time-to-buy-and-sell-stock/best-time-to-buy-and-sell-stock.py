class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        l = 0
        r = 1

        while r < len(prices): 
            # profitable
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else: 
                l = r
            r += 1

        return max_profit