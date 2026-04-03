class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        set_nums = set(nums)
        ans = float('-inf')
        for i in set_nums:
            if i - 1 in set_nums: 
                continue
            curr = 1
            j = i+1
            while True:
                if j in set_nums:
                    curr += 1
                    j += 1
                else: break
            ans = max(curr, ans)
        return ans