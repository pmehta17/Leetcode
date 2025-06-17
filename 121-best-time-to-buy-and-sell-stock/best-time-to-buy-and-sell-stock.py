class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        if len(prices) < 2:
            return 0

        l, r = 0, 1

        while r < len(prices):


            tempProfit = prices[r] - prices[l]
            maxProfit = max(tempProfit, maxProfit)


 
            if prices[l] < prices[r]:
                 r += 1
            elif prices[l] >= prices[r]:
                l = r
                r = l + 1 



        return maxProfit 