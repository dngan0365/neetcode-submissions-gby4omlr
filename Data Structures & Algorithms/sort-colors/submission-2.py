class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for i in nums:
            if i == 0:
                count[0]+=1
            elif i == 1:
                count[1]+=1
            else:
                count[2]+=1
        idx = 0
        for i, cnt in enumerate(count):
            for _ in range(cnt):
                nums[idx] = i
                idx += 1
        return nums
        