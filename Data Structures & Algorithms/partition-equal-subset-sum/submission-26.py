class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_list = sum(nums)
        if sum_list % 2 == 1:
            return False
        target = sum_list // 2
        memo = [False]*(target+1)
        nextDp = [False]*(target+1)

        memo[0] = True

        for i in range(len(nums)):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    nextDp[j] = memo[j] or memo[j - nums[i]]
                else:
                    nextDp[j] = memo[j]
            memo, nextDp = nextDp, memo

        return memo[target]
