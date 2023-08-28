class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        local_min = 100000
        max_profit = 0
        for i in range(len(prices)):
            local_min = min(local_min, prices[i])
            max_profit = max(prices[i]-local_min, max_profit)
        return max_profit