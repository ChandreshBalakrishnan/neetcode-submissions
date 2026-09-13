class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float('inf')

        for p in prices:
            max_profit = max(max_profit, p - min_so_far)
            min_so_far = min(min_so_far, p)
        
        return max_profit