class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        set_nums = set(nums)
        ans = float('-inf')
        for i in set_nums:
            cons = set()
            cons.add(i)
            j = i+1
            while True:
                if j in set_nums:
                    cons.add(j)
                    j += 1
                else: break
            curr = len(cons)
            ans = max(curr, ans)
        return ans
