class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            for j in range(i,len(nums)):

                subset.append(nums[j])

                if sum(subset) > target:
                    print("> targe, i: ", i)
                    # print(subset)
                
                elif sum(subset) == target:
                    print("= targe, i: ", i)
                    print(subset)
                    res.append(subset[:])

                else:
                    dfs(j)

                subset.pop()

        dfs(0)
        return res

# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []
#         subset = []

#         def dfs(i):
#             for j in range(i, len(nums)):
#                 subset.append(nums[j])

#                 s = sum(subset)
#                 if s > target:
#                     # print for debugging
#                     print("> target, i:", i, "subset:", subset)
#                 elif s == target:
#                     print("= target, i:", i, "subset:", subset)
#                     res.append(subset[:])  # append a COPY
#                 else:
#                     dfs(j)  # stay at j to allow reuse

#                 subset.pop()  # backtrack

#         dfs(0)
#         return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)

        return res