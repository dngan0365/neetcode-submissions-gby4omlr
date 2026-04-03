# Broute Force
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(n):
#                 if i != j and nums[i] + nums[j] == target:
#                     return [i, j]

# Sorting
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, value in enumerate(nums):
            A.append([value, i])
        A.sort()
        i = 0
        j = len(nums) - 1
        while i < len(nums) and j >= 0:
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif curr < target:
                i += 1
            else:
                j -= 1














