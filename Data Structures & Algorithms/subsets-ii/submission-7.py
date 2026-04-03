class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curr = []
        nums.sort()
        self.helper(0, nums, curr, subsets)
        return subsets

    def helper(self, i: int, nums: List[int], curr: List[int], subsets: List[List[int]]):
        if i >= len(nums):
            subsets.append(curr.copy())
            return
        curr.append(nums[i])
        self.helper(i+1, nums, curr, subsets)
        curr.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.helper(i+1, nums, curr, subsets)
