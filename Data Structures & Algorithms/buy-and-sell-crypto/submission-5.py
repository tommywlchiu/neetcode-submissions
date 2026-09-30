class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = len(prices)
        l = 0
        r = 1
        max_profit = 0
        while r < p:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)         
            else:
                l = r
            r += 1
        return max_profit
        