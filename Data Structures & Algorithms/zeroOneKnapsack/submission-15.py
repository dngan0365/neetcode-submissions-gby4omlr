# DFS
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(curr: int, currCapacity: int):
            if curr == len(profit):
                return 0
            maxProfit = dfs(curr+1, currCapacity)
            # Add
            temp = currCapacity - weight[curr]
            if temp >= 0:
                curr2 = profit[curr] + dfs(curr+1, temp)
                maxProfit = max(maxProfit, curr2)
            return maxProfit
        
        return dfs(0, capacity)
        
            