class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, a):
            if a == 0:
                return 1
            if a < 0:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in memo:
                return memo[(i, a)]
            take = dfs(i, a - coins[i])
            skip = dfs(i+1, a)
            memo[(i,a)] = take + skip
            return memo[(i, a)]
        print(memo)
        return dfs(0, amount)