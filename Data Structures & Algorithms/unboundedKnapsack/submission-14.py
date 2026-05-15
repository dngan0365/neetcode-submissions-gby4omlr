class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0]*(M+1)
        
        for i in range(N):
            currRow = [0]*(M+1)
            for c in range(1, M+1):
                skip = dp[c]
                if c - weight[i] >= 0:
                    # currRow[c] = profit[i] + dp[c-weight[i]]
                    currRow[c] = profit[i] + currRow[c-weight[i]]
                currRow[c] = max(skip, currRow[c])
            dp = currRow 

        return dp[M]