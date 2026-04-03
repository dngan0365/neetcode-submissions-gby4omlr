# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         left , right = 0, 1
#         n = len(nums)
#         while right < n:
#             if nums[left] != nums[right]:
#                 nums[left + 1] = nums[right]
#                 left += 1
#             right += 1
#         return left + 1

# class Solution:
#     def removeDuplicates(self, nums: List[int]):
#         unique = sorted(set(nums))
#         nums[:len(unique)] = unique
#         return len(unique)

class Solution:
    def removeDuplicates(self, nums: List[int]):
        i = 1
        for j in range(len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        return i



