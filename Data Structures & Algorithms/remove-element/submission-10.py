class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l, r = 0, 0
        for r in range(n):
            if (nums[r] != val):
                nums[l] = nums[r]
                l += 1
        return l;