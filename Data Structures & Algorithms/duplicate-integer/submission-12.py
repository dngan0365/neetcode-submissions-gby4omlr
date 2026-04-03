class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set()
        for num in nums:
            if num in setNums:
                return True
            setNums.add(num)
        return False

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) < len(nums)