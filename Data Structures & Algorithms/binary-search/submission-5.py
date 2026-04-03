class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while l<=h:
            m = (l+h)//2
            if target < nums[m]:
                h = m-1
            elif target > nums[m]:
                l = m+1
            else:
                return m
        return -1
        





















# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l+r)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return -1