class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        L, total, min_len, flag = 0, 0, float("inf"), 0
        for R in range(n):
            total += nums[R]
            print(total)
            while total >= target:
                if min_len > R-L+1:
                    min_len = R-L+1
                    flag = 1
                total -= nums[L]
                L += 1
        return min_len if flag == 1 else 0