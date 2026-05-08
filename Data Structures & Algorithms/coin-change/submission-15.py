class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(
                    dp[x],
                    1 + dp[x - coin]
                )
        return dp[amount] if dp[amount] != INF else -1