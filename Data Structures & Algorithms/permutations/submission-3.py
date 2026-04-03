class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def backtrack(i: int, curr: List[int]):
            if len(curr) == len(nums):
                perms.append(curr.copy())
                return
            if i >= len(nums):
                return 
            for j in range(0, len(nums)):
                if nums[j] not in curr:
                    curr.append(nums[j])
                    backtrack(i+1,curr)
                    curr.pop()
        backtrack(0, [])
        return perms