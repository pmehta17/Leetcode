class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # validity check: do we have enough data? also avoids error at the next step

        if len(prices) < 2:
            return 0

        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            # case 1: right value is greater; take the profit
            if prices[r] > prices[l]:
                max_profit += prices[r] - prices[l]
                l = r 
            # case 2: right value is smaller; update left pointer
            else:
                l = r
            r+=1
        return max_profit
        