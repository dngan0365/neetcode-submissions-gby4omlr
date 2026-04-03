class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            curr_product = 1
            for j in range(len(nums)):
                if i != j:
                    curr_product *= nums[j]
            ans.append(curr_product)
        return ans