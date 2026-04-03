class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = float('-inf')
        min_val = float('inf')
        ans = 0
        n = len(prices)
        for i in range(0, n):
            if prices[i] < min_val:
                min_val = prices[i]
                max_val = float('-inf')
            elif prices[i] > max_val:
                max_val = prices[i]
            print(min_val, " ", max_val)
            curr = max_val - min_val
            if curr > ans:
                ans = curr
        return ans
            