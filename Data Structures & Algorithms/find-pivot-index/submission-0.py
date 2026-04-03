class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0]*(n+1)
        curr = 0
        for i in range(n):
            curr += nums[i]
            preSum[i+1] = curr
        for i in range(1, n+1):
            if preSum[i-1] == preSum[n] - preSum[i]:
                return i-1
        return -1