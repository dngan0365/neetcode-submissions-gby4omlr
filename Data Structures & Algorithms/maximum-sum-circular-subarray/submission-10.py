class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        n = len(nums)
        for i in range(0, n):
            currSum = 0
            for j in range(0, n):
                temp = (i+j) % n
                currSum += nums[temp]
                maxSum = max(maxSum, currSum)
        return maxSum