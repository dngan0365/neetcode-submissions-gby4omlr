class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i: int):
            if i == len(nums):
                return [[]]
            resPerms = []
            perms = backtrack(i+1)
            for p in perms:
                for j in range(0, len(p)+1):
                    curr = p.copy()
                    curr.insert(j, nums[i])
                    resPerms.append(curr)
            return resPerms
        
        perms = backtrack(0)
        return perms