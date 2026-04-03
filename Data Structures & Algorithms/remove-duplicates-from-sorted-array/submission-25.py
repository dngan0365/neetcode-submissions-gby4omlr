class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left , right = 0, 1
        n = len(nums)
        while right < n:
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1
            right += 1
        return left + 1