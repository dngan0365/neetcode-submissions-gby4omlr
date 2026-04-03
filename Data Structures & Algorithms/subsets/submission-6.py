# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         subset = []

#         def trySubsets(i):

#             if i >= len(nums):
#                 res.append(subset.copy())
#                 return

#             subset.append(nums[i])

#             trySubsets(i+1)
#             subset.pop()
#             trySubsets(i+1)

#         trySubsets(0)
#         return res




class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def addSubset(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            addSubset(i+1)
            
            subset.pop()
            addSubset(i+1)

        addSubset(0)
        return res























