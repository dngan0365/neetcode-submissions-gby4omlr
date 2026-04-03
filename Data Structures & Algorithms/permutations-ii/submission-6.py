# Don't work
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtrack(i: int):
            if i == len(nums):
                return [[]]
            resPerm = []
            perms = backtrack(i+1)
            for p in perms:
                for j in range(0, len(p)+1):
                    if (j-1 >= 0 and p[j-1] == nums[i]):
                        continue
                    curr = p.copy()
                    curr.insert(j, nums[i])
                    resPerm.append(curr)
            return resPerm
        
        return backtrack(0)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms, curr = [], []
        self.helper(nums, curr, perms)
        return perms

    def helper(self, nums, curr, perms):
        # all nums are iterated
        if len(nums) == 0:
            perms.append(curr.copy())
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip this entire branch of tree
            curr.append(nums[i])
            remaining = nums[:i] + nums[i+1:]
            self.helper(remaining, curr, perms)
            curr.pop()
