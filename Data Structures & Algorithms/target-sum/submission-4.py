class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dfs
        n = len(nums)
        def dfs(i, curr):
            if i == n and curr == target: 
                return 1
            if i >= n:
                return 0
            return dfs(i+1, curr + nums[i]) + dfs(i+1, curr - nums[i])
        res = dfs(0, 0)
        return res
