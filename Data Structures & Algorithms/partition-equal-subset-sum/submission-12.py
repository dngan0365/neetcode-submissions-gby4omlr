class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_list = sum(nums)
        if sum_list % 2 == 1:
            return False
        target = sum_list // 2
        
        def dfs(i, recent):
            if recent == target:
                return True
            if i >= len(nums) or recent > target:
                return False
            # chọn nums[i]
            if dfs(i + 1, recent + nums[i]):
                return True
            # không chọn nums[i]
            if dfs(i + 1, recent):
                return True
            return False
        
        return dfs(0, 0)

