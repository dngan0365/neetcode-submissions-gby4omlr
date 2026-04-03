class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for i in nums:
            count[i] += 1
        idx = 0
        for i, cnt in enumerate(count):
            for _ in range(cnt):
                nums[idx] = i
                idx += 1
        return nums
        