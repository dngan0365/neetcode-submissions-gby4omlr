class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.helperMaxCapacity(0, profit, weight, capacity)
    
    def helperMaxCapacity(self, i, profit, weight, capacity):
        if i >= len(profit):
            return 0
        # skip
        maxCurr = self.helperMaxCapacity(i+1, profit, weight, capacity)
        newCap = capacity - weight[i]
        if newCap >= 0:
            curr = profit[i] + self.helperMaxCapacity(i, profit, weight, newCap)
            maxCurr = max(maxCurr, curr)
        return maxCurr